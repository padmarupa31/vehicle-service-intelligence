# Advanced Vehicle Service Analytics & Maintenance Insights System

An educational Streamlit dashboard for exploring fictional motorcycle service records.

## Features
- KPI cards: service records, total and average cost, vehicles represented
- Filters for model, service type, date range, and service-cost range
- Interactive service-cost comparison and monthly service activity charts with varied monthly record counts (43 fictional records across Jan–Oct 2026)
- Relative high-cost review flags (not fault prediction or diagnosis)
- Searchable service history table and filtered CSV download

## Tech stack
Python, Pandas, Streamlit, Plotly

## Run locally
1. Extract this ZIP.
2. Open PowerShell in the folder containing `app.py`.
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run: `python -m streamlit run app.py`
5. Open the local URL shown in the terminal (usually http://localhost:8501).

## Data and limitations
The included records are fictional sample data for a student demo. This is not official Royal Enfield data and is not connected to any manufacturer or service database. High-cost flags use the 75th percentile of the currently filtered sample and are review prompts only; they do not diagnose faults or predict failures.
