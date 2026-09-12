# Multi-File Sales Report Generator

## Description

A Python command-line utility that processes one or more sales CSV files and generates combined sales metrics and product performance information.

## Problem

Small businesses often export sales information into separate CSV files. Reviewing multiple exports manually to calculate total revenue, units sold, and product performance can be repetitive and error-prone.

This program automatically discovers sales CSV files in an input directory, processes them together, and generates a combined report.

## Features

- Automatically discovers CSV files in the input folder
- Processes multiple files in one run
- Calculates total revenue
- Calculates total units sold
- Calculates revenue by product
- Identifies the highest-revenue product
- Supports any number of products
- Generates a combined CSV report automatically
- Does not require input files to use a specific filename 
- Validates required CSV headers before processing
- Skips malformed sales rows instead of terminating the program
- Automatically creates the output directory when needed
- Formats revenue values to two decimal places
- Ignores empty product names

## How It Works

1. The program searches the input directory for CSV files.
2. Each CSV file is opened and processed row-by-row.
3. Quantity and unit price values are converted from strings into numeric values.
4. Revenue is calculated for each sales row.
5. Overall revenue and total units sold are accumulated.
6. Revenue is also accumulated separately for each product.
7. After all files have been processed, the product with the highest total revenue is identified.
8. The final metrics are written to a report.

## Expected Input

Each input CSV file should contain the following columns:

```csv
date,product,quantity,unit_price
2026-09-01,Widget A,3,12.50
2026-09-01,Widget B,1,25.00
2026-09-02,Widget A,2,12.50
```

### Required Columns

- `date` — date of the sale
- `product` — product name
- `quantity` — number of units sold
- `unit_price` — price of one unit

Product names do not need to be predefined in the program. New products are discovered automatically while the CSV files are processed.

## Project Structure

```text
multi-file-sales-report/
├── input/
│   ├── sales_week_1.csv
│   └── sales_week_2.csv
├── output/
│   └── report.csv
├── main.py
└── README.md
```

Place any compatible sales CSV files inside the `input` directory before running the program.

The filenames themselves do not matter as long as they end with `.csv`.

## Requirements

- Python 3.10+

This project uses only Python's standard library:

- `csv`
- `pathlib`

No additional packages need to be installed.

## Running the Program

1. Download or clone the project.
2. Place one or more compatible CSV files inside the `input` folder.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

The program will automatically discover and process every `.csv` file inside the input directory.

After processing is complete, the program creates `Output/report.csv`.

## Example Report

The generated report contains overall sales metrics followed by revenue totals for each product.

Example:

```csv
Metric,Value
Total Revenue,2450.75
Total Sold,132
Best Product,Widget A

Product,Revenue
Widget A,1050.25
Widget B,825.50
Widget C,575.00
```

Actual values depend on the contents of the input files.

## Design Decisions

### Multiple Input Files

The program does not require users to rename their sales exports to a specific filename.

Instead, Python's `pathlib` module is used to discover every `.csv` file inside the input directory.

This allows additional sales files to be added without modifying the program.

### Dynamic Product Tracking

Product names are not hard-coded.

A dictionary is used to store revenue totals for each product as products are encountered while processing the input files.

This means the program can process new or previously unseen products without requiring changes to the source code.

### Combined Metrics

Overall metrics are stored separately from product-level metrics.

This keeps global values such as total revenue and total units sold separate from dynamically discovered product names.

### Best-Performing Product

The highest-revenue product is calculated only after all input files have been processed.

This avoids repeatedly calculating the current highest-performing product while data is still being collected.

## Current Limitations

The current version assumes:

- Input files use UTF-8 encoding.
- All sales use the same currency.
- Quantity values represent whole-number units.
- Revenue calculations use Python floating-point numbers.
- All compatible CSV files in the input folder are combined into one report.
- Invalid rows are reported to the console but are not written to a separate error log.
- The program does not currently generate date-based summaries.

## Possible Future Improvements

- Write skipped or invalid records to an error log
- Allow configurable input and output directories
- Add automated tests
- Support Excel files
- Add additional product metrics
- Add date-based sales summaries
- Use Python's `Decimal` type for currency-safe calculations

## What I Learned

This project provided practical experience with:

- Python functions
- CSV parsing and generation
- File handling
- `pathlib`
- Dictionaries and nested dictionaries
- Loops and conditionals
- Type conversion
- Aggregating information across multiple files
- Dynamically handling previously unknown products
- Separating file discovery, data processing, and report generation into different responsibilities

## Author

Created as a practical Python automation and data-processing project.
