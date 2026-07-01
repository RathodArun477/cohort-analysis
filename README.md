# Customer Cohort Analysis — Online Retail II

A cohort analysis of 540,000+ retail transactions, completed as part of a Data Science internship project.

## Objective

Analyze customer retention, revenue trends, and customer lifetime value (CLV) across acquisition cohorts to identify churn patterns and high-value customer segments.

## Dataset

* **Source:** Online Retail II — UCI Machine Learning Repository
* **Period:** December 2010 – December 2011
* **Size:** 541,910 rows, 8 columns

## Tech Stack

* **Python:** Pandas, Matplotlib, Seaborn
* **Power BI:** Interactive dashboard development
* **Jupyter Notebook:** Exploratory data analysis

## Project Structure

```text
cohort-analysis/
├── data/
│   ├── raw/                  # Original dataset (not tracked)
│   └── processed/            # Cleaned CSVs for Power BI
├── notebooks/
│   └── cohort_analysis.ipynb
├── scripts/
│   └── cohort_pipeline.py
├── powerbi/
│   └── cohort_dashboard.pbix
├── report/
│   └── deep_dive_report.md
└── README.md
```

## KPIs

| Metric               | Value   |
| -------------------- | ------- |
| Total Customers      | 4,372   |
| Total Revenue        | £8.91M  |
| Average Order Value  | £480.87 |
| Repeat Purchase Rate | 66%     |
| Average CLV          | £2,050  |

## Key Findings

* 60–80% of customers churn after their first purchase across all cohorts.
* The December 2010 cohort generates the highest lifetime revenue.
* Customers retained beyond Month 3 spend significantly more per order.
* Holiday-season cohorts (November–December) exhibit the strongest retention rates.

## How to Run

```bash
# Install dependencies
pip install pandas matplotlib seaborn

# Run the pipeline from the project root
python scripts/cohort_pipeline.py

# Processed CSVs will be generated in data/processed/
# Import them into Power BI to rebuild the dashboard
```

## Dashboard

Built in Power BI Desktop, featuring:

* KPI cards (5 core metrics)
* Cohort retention heatmap
* Revenue trend by cohort
* AOV by cohort index
* Month 1 drop-off rate by cohort

