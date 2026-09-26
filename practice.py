import pandas as pd 
import numpy as np 


file_name = input("Enter file name (csv / xlsx) : ")

try:
    if file_name.endswith(".csv"):
        df = pd.read_csv(file_name)

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(file_name)

    else:
        print("Unsupported file")
        exit()

except FileNotFoundError:
    print("File not found.")
    exit()


# String columns
string_columns = [
    "Order ID",
    "Customer ID",
    "City",
    "Category",
    "Product",
    "Payment Mode",
    "Order Status"
]

for col in string_columns:
    df[col] = df[col].astype("string")


# Date column
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)


# Integer column
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
).astype("Int64")


# Float columns
float_columns = [
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

for col in float_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    ).astype("float64")


# Check data types
print(df.dtypes)

    # Upper/lower inconsistency fix
for col in df.columns:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.title()
    )

print("Upper/Lower case inconsistency fixed!")

# -------------------------------
# 1. Date Column
# -------------------------------
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Missing dates ko median date se fill
df["Order Date"] = df["Order Date"].fillna(
    df["Order Date"].dropna().median()
)


# -------------------------------
# 2. Categorical / Text Columns
# -------------------------------

for col in df.columns:
    df[col] = df[col].astype("string").str.strip()
    df[col] = df[col].fillna("Unknown")


# -------------------------------
# 3. Numeric Columns
# -------------------------------


for col in df.columns:
    # Text ko numeric me convert
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

    # Missing values ko median se fill
    df[col] = df[col].fillna(
        df[col].median()
    )


# -------------------------------
# 4. Check Missing Values
# -------------------------------
print("Missing Values After Cleaning:")

print(
    df.isnull().sum()
)


# -------------------------------
# 5. Save changes in df
# -------------------------------
print("\nData Missing value handled Completed!")

# Duplicate rows check
print("Duplicate rows:", df.duplicated().sum())

# Duplicate rows remove
df.drop_duplicates(inplace=True)

# Check again
print("Duplicate rows after cleaning:", df.duplicated().sum())

# String columns
string_columns = [
    "Order ID",
    "Customer ID",
    "City",
    "Category",
    "Product",
    "Payment Mode",
    "Order Status"
]

for col in string_columns:
    df[col] = (
        df[col]
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

# Step 1: Remove extra spaces
df["Order Status"] = df["Order Status"].str.strip()

# Step 2: Convert to lowercase
df["Order Status"] = df["Order Status"].str.lower()

# Step 3: Fix inconsistent values
status_mapping = {
    "complete": "Completed",
    "completed": "Completed",
    "pending": "Pending",
    "cancelled": "Cancelled",
    "canceled": "Cancelled",
    "returned": "Returned"
}

df["Order Status"] = df["Order Status"].replace(status_mapping)


# Original data ko string format me temporarily rakho
original_dates = df["Order Date"].copy()

# Convert date
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Invalid dates identify karo
invalid_dates = original_dates[
    df["Order Date"].isna() &
    original_dates.notna()
]

# Invalid dates print karo
print("Invalid Dates:")
print(invalid_dates)

# Invalid dates ki total count
print("\nTotal Invalid Dates:", len(invalid_dates))

# Find negative prices
negative_price = df[df["Unit Price"] < 0]

print("Negative Unit Price:")
print(negative_price)

# Convert negative values to missing
df.loc[df["Unit Price"] < 0, "Unit Price"] = np.nan

# Fill missing values with median
df["Unit Price"] = df["Unit Price"].fillna(
    df["Unit Price"].median()
)

# Check again
print("\nNegative values after cleaning:")
print((df["Unit Price"] < 0).sum())

numeric_columns = [
    "Quantity",
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )
    
columns = [
    "Order ID",
    "Customer ID",
    "City",
    "Order Date",
    "Category",
    "Product",
    "Quantity",
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit",
    "Payment Mode",
    "Order Status"
]

for col in columns:
    print("\n" + "=" * 50)
    print("Column:", col)
    print("Unique values:", df[col].nunique(dropna=True))
    print("Unique values:")
    print(df[col].dropna().unique())