import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Dataset
all_df = pd.read_csv("all_data.csv")

# Konversi datetime_cols ke dalam tipe data datetime
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

# Sidebar
with st.sidebar:
    st.write('# Projek Akhir Muhammad Raihan Ramadhan :sparkles:')
    st.image("bangkit.jpg", caption="Bangkit 2024", use_column_width=True,)
    min_date = all_df["order_approved_at"].min().date()
    max_date = all_df["order_approved_at"].max().date()
    start_date = st.date_input(label="Start Date", value=min_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input(label="End Date", value=max_date, min_value=min_date, max_value=max_date)

# Main
main_df = all_df[(all_df["order_approved_at"] >= str(start_date)) & (all_df["order_approved_at"] <= str(end_date))]

# Visualisasi
st.title("E-Commerce Data Analysis Dashboard")

# Deskripsi
st.write("**This dashboard provides insights into E-Commerce public data.**")

# Visualisasi 1: Daily Orders Delivered
st.header("Daily Orders Delivered")

# Total Orders and Revenue
total_orders = main_df["order_id"].nunique()
total_revenue = main_df["price"].sum()
st.write(f"Total Orders: {total_orders}")
st.write(f"Total Revenue: ${total_revenue}")

# Daily Orders Line Plot
daily_orders = main_df.set_index("order_approved_at").resample("D")["order_id"].nunique()
plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_orders.index, y=daily_orders.values, marker="o", linewidth=2, color="#4CAF50")
plt.title("Daily Orders Delivered", fontsize=20, fontweight='bold', color='#333333')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Orders", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
st.pyplot(plt.gcf())  

# Visualisasi 2: Customer Spend Money
st.header("Customer Spend Money")

# Total Spend and Average Spend per Customer
total_spend = main_df.groupby("customer_id")["price"].sum().sum()
avg_spend = main_df.groupby("customer_id")["price"].sum().mean()
st.write(f"Total Spend: ${total_spend}")
st.write(f"Average Spend per Customer: ${avg_spend:.2f}")

# Customer Spend Distribution Histogram
customer_spend = main_df.groupby("customer_id")["price"].sum()
plt.figure(figsize=(12, 6))
sns.histplot(customer_spend, bins=20, color="#FF6D00", kde=True)
plt.title("Distribution of Customer Spend Money", fontsize=20, fontweight='bold', color='#333333')
plt.xlabel("Total Spend", fontsize=14)
plt.ylabel("Number of Customers", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
st.pyplot(plt.gcf())  

# Visualisasi 3: Order Items
st.header("Order Items")

# Total Items and Average Items per Order
total_items = main_df["order_item_id"].count()
avg_items = main_df["order_item_id"].mean()
st.write(f"Total Items: {total_items}")
st.write(f"Average Items per Order: {avg_items:.2f}")

# Top 5 and Bottom 5 Product Categories
top_5_categories = main_df["product_category_name"].value_counts().head(5)
bottom_5_categories = main_df["product_category_name"].value_counts().tail(5)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_5_categories.values, y=top_5_categories.index, palette="viridis")
plt.title("Top 5 Product Categories", fontsize=20, fontweight='bold', color='#333333')
plt.xlabel("Number of Orders", fontsize=14)
plt.ylabel("Product Category", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
st.pyplot(plt.gcf())  

plt.figure(figsize=(12, 6))
sns.barplot(x=bottom_5_categories.values, y=bottom_5_categories.index, palette="viridis")
plt.title("Bottom 5 Product Categories", fontsize=20, fontweight='bold', color='#333333')
plt.xlabel("Number of Orders", fontsize=14)
plt.ylabel("Product Category", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
st.pyplot(plt.gcf())  
