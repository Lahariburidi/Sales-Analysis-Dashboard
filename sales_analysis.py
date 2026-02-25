import pandas as pd
import matplotlib.pyplot as plt

# ===== Load dataset =====
df = pd.read_csv("sales_data.csv")

# Convert Order_Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M')

# ===== KPI =====
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)

# ===== Revenue by Region =====
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
region_revenue.plot(kind='bar', color='skyblue')
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.xlabel("Region")
for i, val in enumerate(region_revenue):
    plt.text(i, val, f'{val:,.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()  # waits until you close it

# ===== Monthly Revenue =====
monthly_revenue = df.groupby('Month')['Revenue'].sum()
plt.figure(figsize=(8,5))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title("Monthly Revenue")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()
plt.show()  # waits until you close it

# ===== Top 5 Customers =====
top_customers = df.groupby('Customer_ID')['Revenue'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
top_customers.plot(kind='bar', color='orange')
plt.title("Top 5 Customers by Revenue")
plt.ylabel("Revenue")
plt.xlabel("Customer ID")
for i, val in enumerate(top_customers):
    plt.text(i, val, f'{val:,.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()  # waits until you close it

# Optional: pause at end so terminal stays
input("Press Enter to exit...")
