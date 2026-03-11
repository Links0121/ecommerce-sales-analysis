import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../datas/Ecommerce_data.csv")

# Preview data
print(df.head())

# Data structure
print(df.info())

# Summary statistics
print(df.describe())

# Convert order date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly sales trend
sales_trend = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
sales_trend.plot(figsize=(10, 5), title="Monthly Sales Trend")
plt.tight_layout()
plt.show()

# Category sales
category_sales = df.groupby("Category")["Sales"].sum().sort_values()
category_sales.plot(kind="barh", title="Sales by Category")
plt.tight_layout()
plt.show()

# Regional sales
region_sales = df.groupby("Region")["Sales"].sum()
region_sales.plot(kind="bar", title="Sales by Region")
plt.tight_layout()
plt.show()
