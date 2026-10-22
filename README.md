# Vehicle Service Intelligence
### Vehicle Service Data Analytics & Maintenance Insights Dashboard

An interactive data analytics dashboard built with Python to explore motorcycle service records, analyze maintenance costs, and identify service activity trends through clear visualizations.

**Live Demo:** [Vehicle Service Intelligence Dashboard](https://vehicle-service-intelligence.onrender.com/)  
**Source Code:** [GitHub Repository](https://github.com/padmarupa31/vehicle-service-intelligence)

---

## Overview

Vehicle Service Intelligence is a data analytics project designed to help users explore motorcycle service history and understand maintenance cost patterns. The dashboard provides interactive filters, key performance indicators, visual analytics, and searchable service records in one interface.

The project demonstrates how Python-based data analysis and visualization tools can transform structured service records into useful insights.

## Key Features

- **Service KPI Dashboard** — View total service records, total maintenance cost, average service cost, and vehicles represented.
- **Interactive Filters** — Filter records by vehicle model, service type, service date, and cost range.
- **Maintenance Cost Analysis** — Compare service costs across vehicle models using interactive charts.
- **Monthly Service Trends** — Explore changes in service activity across months.
- **High-Cost Review** — Highlight relatively high-cost records for further review using a percentile-based threshold.
- **Searchable Service History** — Find and review individual service records.
- **CSV Export** — Download filtered service records for further analysis.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Pandas | Data cleaning, filtering, and analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive data visualizations |

## Project Structure

```text
vehicle-service-intelligence/
├── app.py
├── service_data.csv
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- pip package manager

### Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/padmarupa31/vehicle-service-intelligence.git
   ```

2. Navigate to the project directory:

   ```bash
   cd vehicle-service-intelligence
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the dashboard:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Dataset and Limitations

- The dashboard uses **43 fictional sample service records** covering January–October 2026.
- The dataset is intended for educational demonstration and does not represent actual customer, vehicle, or service-centre records.
- This project is not affiliated with or connected to Royal Enfield or any manufacturer's internal systems.
- High-cost flags are relative review indicators based on the 75th percentile of the currently filtered data. They are not mechanical diagnoses, fault predictions, or official maintenance recommendations.
- The sample dataset is intended to demonstrate analytics workflows; conclusions should not be treated as real-world operational findings.

## Future Enhancements

- Integrate verified, real-world service data where authorized.
- Add richer time-series analysis and service-cost comparisons.
- Introduce configurable maintenance reminders based on verified manufacturer guidance.
- Add automated data validation and reporting features.

## Author

**Padmaroopa D.**

---

*Developed as an educational project to demonstrate Python-based data analysis, interactive visualization, and dashboard development.*
