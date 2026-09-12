# Multi-File Sales Report Generator

## Description

A Python command-line utility that processes one or more sales CSV files and generates a combined sales report with revenue, units sold, product performance, and the overall sales timeframe.

## Problem

Small businesses often export sales information into separate CSV files. Reviewing multiple exports manually to calculate total revenue, units sold, product performance, and reporting periods can be repetitive and error-prone.

This program automatically discovers sales CSV files in an input directory, validates them, processes all valid records together, and generates a combined report.

## Features

- Automatically discovers CSV files in the input folder
- Processes multiple files in one run
- Validates required CSV headers before processing
- Skips malformed or invalid rows without terminating the program
- Calculates total revenue
- Calculates total units sold
- Calculates revenue by product
- Identifies the highest-revenue product
- Reports the earliest and latest valid sale dates
- Supports any number of products
- Trims unnecessary whitespace from product names
- Automatically creates the output directory when needed
- Generates a combined CSV report
- Does not require input files to use a specific filename

## How It Works

1. The program searches the input directory for `.csv` files.
2. Each file is checked for the required columns.
3. Files missing required columns are skipped.
4. Valid files are processed row-by-row.
5. Quantity and unit price values are converted to numeric types.
6. Sale dates are parsed and used to determine the overall reporting timeframe.
7. Invalid rows are skipped and reported in the console.
8. Revenue is calculated for each valid sale.
9. Overall and per-product metrics are accumulated across all valid input files.
10. The highest-revenue product is determined after all files have been processed.
11. The final metrics are written to `output/report.csv`.

## Expected Input

Each input CSV file should contain the following columns:

```csv
date,product,quantity,unit_price
2026-09-01,Widget A,3,12.50
2026-09-01,Widget B,1,25.00
2026-09-02,Widget A,2,12.50
```

### Required Columns

- `date` — date of the sale in `YYYY-MM-DD` format
- `product` — product name
- `quantity` — number of units sold
- `unit_price` — price of one unit

Product names do not need to be predefined in the program. New products are discovered automatically while the files are processed.

## Project Structure

```text
multi-file-sales-report-generator/
├── input/
│   ├── sales_week_1.csv
│   └── sales_week_2.csv
├── output/
│   └── report.csv
├── test_data/
│   ├── sales_error_test.csv
│   └── sales_missing_column.csv
├── main.py
├── README.md
└── .gitignore
```

The `test_data` directory is optional and contains intentionally invalid sample data used to verify error handling.

## Requirements

- Python 3.10 or newer

This project uses only Python's standard library.

Modules used include:

- `csv`
- `pathlib`
- `datetime`
- `typing`

No third-party packages are required.

## Running the Program

1. Download or clone the repository.
2. Place one or more compatible CSV files inside the `input` folder.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

The program automatically discovers and processes every `.csv` file inside the input directory.

After processing is complete, the report is created at:

```text
output/report.csv
```

## Example Report

The generated report contains overall sales metrics followed by revenue totals for each product.

Example:

```csv
Metric,Value
Report Timeframe,2026-09-01 to 2026-09-11
Total Revenue,2450.75
Total Sold,132
Best Product,Widget A

Product,Revenue
Widget A,1050.25
Widget B,825.50
Widget C,575.00
```

Actual values depend on the contents of the input files.

## Error Handling

The program is designed to continue processing when possible instead of terminating because of one invalid record.

Examples of invalid data that are skipped include:

- Non-numeric quantities
- Invalid unit prices
- Empty product names
- Invalid date formats

Entire CSV files are skipped when they do not contain all required columns.

Skipped rows and files are reported in the console so the user can identify problems in the source data.

## Design Decisions

### Multiple Input Files

The program does not require users to rename exports to a specific filename.

Python's `pathlib` module is used to discover every `.csv` file inside the input directory. This allows additional sales files to be added without modifying the source code.

### Dynamic Product Tracking

Product names are not hard-coded.

A dictionary stores revenue totals for each product as products are encountered. This allows previously unseen products to be processed automatically.

### Combined Metrics

Overall metrics are stored separately from product-level metrics.

This keeps values such as total revenue and total units sold separate from dynamically discovered product names.

### Best-Performing Product

The highest-revenue product is calculated only after all files have been processed.

This avoids repeatedly calculating the current best-performing product while data is still being collected.

### Sales Timeframe

The program uses valid sale dates across all processed files to determine the earliest and latest dates represented in the final report.

### Safer Input Processing

Input files are validated before processing, and malformed individual rows are skipped rather than causing the full report generation process to fail.

## Current Limitations

The current version assumes:

- Input CSV files use UTF-8 encoding.
- Dates use the `YYYY-MM-DD` format.
- Quantity values represent whole-number units.
- All sales use the same currency.
- Revenue calculations use Python floating-point numbers.
- All compatible CSV files in the input folder should be combined into one report.
- Invalid rows are reported to the console but are not written to a separate error log.

## Testing

The program was manually tested with:

- Multiple valid CSV files
- Repeated products across multiple files
- New products appearing in later files
- Invalid quantity values
- Invalid unit prices
- Empty product names
- Invalid date formats
- CSV files missing required columns

The program continues processing valid data while reporting invalid rows and incompatible files to the console.

## Possible Future Improvements

- Add automated tests with `pytest`
- Write skipped rows and files to a dedicated error log
- Allow configurable input and output directories
- Support Excel files
- Add additional product metrics
- Add daily, weekly, or monthly sales summaries
- Allow filtering by a requested date range
- Use Python's `Decimal` type for currency-safe calculations

## What I Learned

This project provided practical experience with:

- Python functions
- CSV parsing and generation
- File handling
- `pathlib`
- Dictionaries and nested dictionaries
- Typed dictionaries and type hints
- Loops and conditionals
- Type conversion
- Date parsing and comparison
- Input validation
- Error handling
- Aggregating information across multiple files
- Dynamically handling previously unknown products
- Separating file discovery, data processing, and report generation into different responsibilities

## Author

Created as a practical Python automation and data-processing portfolio project.
