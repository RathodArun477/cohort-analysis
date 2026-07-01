import pandas as pd
import os

RAW_PATH = 'data/raw/online_retail_II.csv'
PROCESSED_DIR = 'data/processed'

os.makedirs(PROCESSED_DIR,exist_ok=True)

print("Loading data...")
df = pd.read_csv(RAW_PATH,encoding='latin1')
print(f"Raw shape: {df.shape}")

df.dropna(subset=['Customer ID'],inplace=True)
df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0]
df = df[~df['Invoice'].astype(str).str.startswith('C')] 

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Customer ID'] = df['Customer ID'].astype(int)
df['Revenue'] = df['Quantity'] * df['Price']
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

print(f"Clean shape: {df.shape}")

df['CohortMonth'] = df.groupby('Customer ID')['InvoiceMonth'].transform('min')
df['CohortIndex'] = (df['InvoiceMonth'] - df['CohortMonth']).apply(lambda x: x.n)

cohort_data = (
    df.groupby(['CohortMonth','CohortIndex'])['Customer ID'].nunique().reset_index().rename(columns={'Customer ID': 'Customers'})
)

cohort_pivot  = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='Customers')
cohort_size   = cohort_pivot[0]
retention_pct = cohort_pivot.divide(cohort_size, axis=0).round(4)

retention_flat = (
    retention_pct
    .reset_index()
    .melt(id_vars='CohortMonth', var_name='CohortIndex', value_name='RetentionRate')
    .dropna()
)

revenue_data = (
    df.groupby(['CohortMonth', 'CohortIndex'])['Revenue']
    .sum()
    .reset_index()
    .rename(columns={'Revenue': 'TotalRevenue'})
)

order_revenue = df.groupby(['CohortMonth', 'CohortIndex', 'Invoice'])['Revenue'].sum().reset_index()
aov_data = (
    order_revenue.groupby(['CohortMonth', 'CohortIndex'])['Revenue']
    .mean()
    .reset_index()
    .rename(columns={'Revenue': 'AOV'})
)

total_customers  = df['Customer ID'].nunique()
total_revenue    = df['Revenue'].sum()
aov_overall      = df.groupby('Invoice')['Revenue'].sum().mean()
repeat_customers = df.groupby('Customer ID')['Invoice'].nunique()
repeat_rate      = (repeat_customers > 1).sum() / total_customers
avg_clv          = df.groupby('Customer ID')['Revenue'].sum().mean()

kpi_summary = pd.DataFrame([{
    'TotalCustomers'     : total_customers,
    'TotalRevenue'       : round(total_revenue, 2),
    'AOV'                : round(aov_overall, 2),
    'RepeatPurchaseRate' : round(repeat_rate, 4),
    'AvgCLV'             : round(avg_clv, 2)
}])

print("\n── KPI Summary ──")
print(kpi_summary.to_string(index=False))

cohort_data.to_csv(f'{PROCESSED_DIR}/cohort_retention.csv', index=False)
retention_flat.to_csv(f'{PROCESSED_DIR}/cohort_retention_pct.csv', index=False)
revenue_data.to_csv(f'{PROCESSED_DIR}/cohort_revenue.csv', index=False)
aov_data.to_csv(f'{PROCESSED_DIR}/cohort_aov.csv', index=False)
kpi_summary.to_csv(f'{PROCESSED_DIR}/kpi_summary.csv', index=False)

print("\nExported all files to data/processed/")
print("Done.")