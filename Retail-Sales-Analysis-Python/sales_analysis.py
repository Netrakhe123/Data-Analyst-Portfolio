import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df= pd.read_excel("sales_data.xlsx")

# Data Cleaning
print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nData Types")
print(df.dtypes)

# Save Cleaned Data
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("\nCleaned dataset saved successfully.")

# Create Total Sales column   #Calculate Total Sales
df["Sales"]= df["Quantity"] * df["Price"]

# Display all records
#print(df)
# Display first 5 rows
print(df.head())

#Find Total Sales
total_sales = df["Sales"].sum()
#df["Sales"] → Selects the Sales column.
#.sum() → Adds all the sales values together.
print("\nTotal Sales:")
print(total_sales)

# Calculate Average Sales
average_sales=df["Sales"].mean()
print("\nAverage Sales:")
print(average_sales)

# Find Highest Sale
highest_sale=df["Sales"].max()
print("\nHighest Sale:")
print(highest_sale)

# Find Lowest Sale
lowest_sale = df["Sales"].min()
print("\nlowest sale:")
print(lowest_sale)

# Top Selling Products
top_products = df.groupby("Product")["Sales"].sum()
#Groups all rows by Product
print("\nTop Selling Products:")
print(top_products)

# Highest Selling Product
highest_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nHighest Selling Product:")
print(highest_product)
#sort_values(ascending=False)
#Sorts the products from highest sales to lowest sales.

# Top Selling Region
top_regions = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nTop Selling Regions:")
print(top_regions)

 # Convert Date column into Date format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
# OR df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Create Month column
df["Month"] = df["Date"].dt.month_name()

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nmonthly Sales:")
print(monthly_sales)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(top_products.index, top_products.values)
plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/bar_chart.png")
plt.show()

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/line_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(top_regions.values,
        labels=top_regions.index,
        autopct="%1.1f%%")
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("Charts/pie_chart.png")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Charts/histogram.png")
plt.show()

































#print("\nLast 5 Rows")
#print(df.tail())

   #Number of rows and columns
#print("\nShape")
#print(df.shape)
  #Column names
#print("\nColumn Names")
#print(df.columns)
  #Data type of each column
#print("\nData Types")
#print(df.dtypes)


#import = bring a library into our program.
#pandas = Python library used for data analysis.
#as pd = gives pandas a short name (pd) so we don't have to type pandas every time.

#pd.read_excel() reads the Excel file.
#"data/sales_data.xlsx" is the path to your file.
#df stands for DataFrame, which is like a table in Excel.
#Prints all the data from the Excel file in the terminal.