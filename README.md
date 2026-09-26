# Data Cleaning Tool 🧹

A Python-based **Data Cleaning Tool** built using **Pandas** and **NumPy**. 

This project is designed to clean, validate, transform, and analyze raw CSV/Excel datasets before 
using them for Data Analysis or Data Visualization.

## 📌 Project Overview

Raw datasets often contain missing values, duplicate records, extra spaces, inconsistent text formatting, invalid dates, incorrect data types, and other data-quality 
problems.

This tool performs several data-cleaning operations automatically and displays useful information about the dataset.

## ✨ Features

### 1. CSV and Excel File Support

The tool can read both:

* `.csv`

* `.xlsx`

```python

pd.read_csv()

pd.read_excel()

```

### 2. Data Type Conversion

The project converts columns into appropriate data types.

**String columns:**

* Order ID

* Customer ID

* City

* Category

* Product

* Payment Mode

* Order Status

**Integer column:**

* Quantity

**Float columns:**

* Unit Price

* Discount

* Sales

* Cost

* Profit

**Date column:**

* Order Date

### 3. Inconsistent Capitalization Handling

The tool standardizes text formatting using:

```python

.str.strip()

.str.title()

```

For example:

```text

delhi

DELHI

Delhi

```

can be standardized to:

```text

Delhi

```

### 4. Extra Spaces Handling

Unnecessary spaces are removed from text values.

Example:

```text

"  Delhi   "

```

becomes:

```text

"Delhi"

```

### 5. Missing Values Handling

The project checks missing values and handles them using different methods.

* Missing dates → Median date

* Missing text values → `Unknown`

* Missing numeric values → Median value


### 6. Duplicate Rows Handling

The tool first checks the number of duplicate rows:

```pyt
```
