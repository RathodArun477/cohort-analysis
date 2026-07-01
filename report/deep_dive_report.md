# Deep-Dive Analysis Report — Customer Cohort Analysis
**Dataset:** Online Retail II (UCI Machine Learning Repository)  
**Tool:** Python (Pandas, Matplotlib, Seaborn) + Power BI  
**Author:** Arun Rathod  
**Date:** 1st July 2025

---

## 1. Objective

To analyze customer retention, revenue trends, and lifetime value across acquisition cohorts for a UK-based online retailer. The goal is to identify when customers churn, which cohorts are most valuable, and how order value evolves over time.

---

## 2. Dataset Overview

| Property | Detail |
|---|---|
| Source | Online Retail II — UCI / Kaggle |
| Period | December 2010 – December 2011 |
| Raw Rows | 541,910 |
| Columns | Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country |

**Cleaning steps applied:**
- Dropped rows with missing `Customer ID` (~135,080 rows)
- Removed cancelled invoices (Invoice starting with `C`)
- Filtered out negative or zero `Quantity` and `Price`
- Computed `Revenue = Quantity × Price`

**Clean dataset used for analysis:** ~397,000 rows

---

## 3. Core KPIs

| KPI | Formula | Business Rationale |
|---|---|---|
| **Retention Rate** | Customers in month N ÷ Cohort size at month 0 | Measures how well the business holds onto acquired customers |
| **Total Revenue** | Sum of Quantity × Price | Top-line health indicator |
| **Average Order Value (AOV)** | Total Revenue ÷ Number of Orders | Tracks spending behavior per transaction |
| **Repeat Purchase Rate** | Customers with >1 invoice ÷ Total customers | Signals loyalty and product-market fit |
| **Average Customer Lifetime Value (CLV)** | Total Revenue ÷ Total Customers | Long-term revenue potential per customer |

---

## 4. Cohort Analysis — Methodology

Each customer is assigned a **cohort month** equal to the month of their first purchase. For every subsequent month they make a purchase, a **cohort index** (months since first purchase) is recorded.

This produces a cohort matrix where:
- **Rows** = cohort month (when the customer first bought)
- **Columns** = months since first purchase (0, 1, 2, …)
- **Values** = % of original cohort still active

---

## 5. Key Findings

### 5.1 Retention

- **Month 0 → Month 1 drop-off is the steepest across all cohorts** — typically 60–80% of customers do not return after their first purchase.
- Cohorts acquired in **November–December 2010** show relatively stronger retention, likely due to holiday season engagement.
- After Month 3, retention stabilizes at a low but consistent level (~20–30% for the strongest cohorts), indicating a loyal customer base forms early.

### 5.2 Revenue

- The **December 2010 cohort** generates the highest cumulative revenue, driven by both cohort size and repeat purchasing.
- Revenue per cohort spikes at Month 0 (acquisition month) and drops sharply at Month 1, mirroring the retention curve.
- Some cohorts show a **revenue spike at Month 11–12**, likely driven by anniversary re-engagement or seasonal restocking behavior.

### 5.3 Average Order Value

- AOV is **highest in the later cohort indices** (Months 6–12), suggesting that customers who stick around spend more per order over time.
- This is a strong signal: retained customers are not just loyal, they are more valuable per transaction.

### 5.4 Repeat Purchase Rate

- Approximately **35–40% of customers made more than one purchase**, which is healthy for a wholesale/retail context but leaves significant room for retention campaigns.

---

## 6. Business Recommendations

| Finding | Recommendation |
|---|---|
| High Month 0 → 1 churn | Introduce a post-purchase email sequence within 30 days of first order |
| Late-cohort AOV is higher | Target re-engagement campaigns at the 3–6 month mark before customers fully churn |
| Holiday cohorts retain better | Increase acquisition spend in Q4; these customers have higher LTV |
| Stable loyal base after Month 3 | Build a loyalty or subscription program to formalize the repeat-buyer segment |

---

## 7. Dashboard

The interactive Power BI dashboard (`powerbi/cohort_dashboard.pbix`) surfaces:
- KPI cards: Total Customers, Total Revenue, AOV, Repeat Rate, Avg CLV
- Cohort retention heatmap (matrix with conditional formatting)
- Revenue trend by cohort (line chart)
- AOV by cohort index (bar chart)
- Month 1 drop-off rate by cohort (bar chart)
- Filters: Cohort Month, Country

---

## 8. Files

cohort-analysis/
├── data/
│   ├── raw/online_retail_II.csv
│   └── processed/
│       ├── cohort_retention.csv
│       ├── cohort_retention_pct.csv
│       ├── cohort_revenue.csv
│       ├── cohort_aov.csv
│       └── kpi_summary.csv
├── notebooks/cohort_analysis.ipynb
├── scripts/cohort_pipeline.py
├── powerbi/cohort_dashboard.pbix
└── report/
├── deep_dive_report.md
├── kpi_cards.png
├── retention_heatmap.png
├── cohort_revenue.png
├── aov_by_cohort_index.png
└── dropoff_rate.png

---

*Analysis performed as part of Data Science Internship — Task 3: Deep-Dive Analysis & Interactive Dashboarding.*