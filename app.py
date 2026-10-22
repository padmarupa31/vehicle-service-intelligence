import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Vehicle Service Intelligence", page_icon="🏍️", layout="wide")
DATA_FILE = Path(__file__).parent / "service_data.csv"

st.markdown("""
<style>
.block-container {padding-top:1.5rem;padding-bottom:2rem}
[data-testid="stMetric"] {background:linear-gradient(135deg,#1b2638,#222f45);border:1px solid #34445d;padding:16px 18px;border-radius:14px}
[data-testid="stMetricLabel"] {color:#cbd5e1}
[data-testid="stMetricValue"] {color:#f8fafc}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df["Service Date"] = pd.to_datetime(df["Service Date"], errors="coerce")
    df["Service Cost"] = pd.to_numeric(df["Service Cost"], errors="coerce").fillna(0)
    df["Odometer (km)"] = pd.to_numeric(df["Odometer (km)"], errors="coerce").fillna(0)
    return df.dropna(subset=["Service Date"])

df = load_data()
st.sidebar.title("🔎 Explore records")
models = sorted(df["Vehicle Model"].dropna().unique().tolist())
services = sorted(df["Service Type"].dropna().unique().tolist())
chosen_models = st.sidebar.multiselect("Vehicle model", models, default=models)
chosen_services = st.sidebar.multiselect("Service type", services, default=services)
min_date, max_date = df["Service Date"].min().date(), df["Service Date"].max().date()
date_range = st.sidebar.date_input("Service date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
max_cost = max(1000, int(df["Service Cost"].max()))
cost_range = st.sidebar.slider("Service cost range (₹)", 0, max_cost, (0, max_cost), step=500)
st.sidebar.caption("Fictional sample data; not real manufacturer records.")

filtered = df[df["Vehicle Model"].isin(chosen_models) & df["Service Type"].isin(chosen_services)]
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    filtered = filtered[(filtered["Service Date"].dt.date >= date_range[0]) & (filtered["Service Date"].dt.date <= date_range[1])]
filtered = filtered[filtered["Service Cost"].between(cost_range[0], cost_range[1])]

st.title("🏍️ Vehicle Service Intelligence")
st.caption("Interactive service analytics • maintenance trends • cost review")
st.write("Explore sample motorcycle maintenance records and service-cost patterns.")
if filtered.empty:
    st.warning("No records match these filters. Try widening the selected filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Service records", f"{len(filtered):,}")
c2.metric("Total service cost", f"₹{filtered['Service Cost'].sum():,.0f}")
c3.metric("Average service cost", f"₹{filtered['Service Cost'].mean():,.0f}")
c4.metric("Vehicles represented", f"{filtered['Vehicle ID'].nunique():,}")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("Service cost by vehicle model")
    model_cost = filtered.groupby("Vehicle Model", as_index=False)["Service Cost"].sum().sort_values("Service Cost", ascending=False)
    fig = px.bar(model_cost, x="Vehicle Model", y="Service Cost", color="Vehicle Model", text_auto=".2s", title="Total recorded service cost")
    fig.update_layout(showlegend=False, margin=dict(l=10,r=10,t=45,b=10), yaxis_title="Cost (₹)", xaxis_title="")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Monthly service activity")
    monthly = filtered.assign(Month=filtered["Service Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False).size().rename(columns={"size":"Service Records"})
    fig2 = px.line(monthly, x="Month", y="Service Records", markers=True, text="Service Records", title="Number of records by month")
    fig2.update_layout(margin=dict(l=10,r=10,t=45,b=10), xaxis_title="", yaxis_title="Records")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.subheader("🧰 Maintenance insights")
threshold = float(filtered["Service Cost"].quantile(0.75))
flagged = filtered[filtered["Service Cost"] > threshold].sort_values("Service Cost", ascending=False)
a, b, c = st.columns(3)
a.metric("Highest recorded cost", f"₹{filtered['Service Cost'].max():,.0f}")
b.metric("75th-percentile threshold", f"₹{threshold:,.0f}")
c.metric("Records flagged for review", f"{len(flagged):,}")
if not flagged.empty:
    st.warning("These records have relatively high costs within the selected sample. This is a review flag, not a mechanical diagnosis.")
    st.dataframe(flagged[["Service ID","Vehicle ID","Vehicle Model","Service Date","Service Type","Service Cost","Odometer (km)","Notes"]], use_container_width=True, hide_index=True)
else:
    st.info("No records exceed the review threshold in this filtered view.")

st.divider()
st.subheader("📋 Service history explorer")
query = st.text_input("Search by service ID, vehicle ID, model, service type, or notes", placeholder="Example: VS-1001 or oil change")
records = filtered.copy()
if query.strip():
    q = query.strip().lower()
    mask = records.astype(str).apply(lambda col: col.str.lower().str.contains(q, na=False)).any(axis=1)
    records = records[mask]
records = records.sort_values("Service Date", ascending=False)
st.caption(f"Showing {len(records)} of {len(filtered)} filtered records.")
st.dataframe(records, use_container_width=True, hide_index=True)
st.download_button("⬇️ Download filtered records (CSV)", records.to_csv(index=False).encode("utf-8"), "filtered_service_records.csv", "text/csv")
with st.expander("ℹ️ Project notes and limitations"):
    st.write("This educational demo uses fictional data and is not connected to Royal Enfield. High-cost flags are based on the selected sample and do not diagnose faults or predict failures.")
