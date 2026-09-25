import csv
from datetime import date
from pathlib import Path
from typing import TypedDict

BASE_FOLDER = Path(__file__).resolve().parent
INPUT_FOLDER = BASE_FOLDER / "input"
OUTPUT_FOLDER = BASE_FOLDER / "output"

REQUIRED_COLUMNS = {"date", "product", "quantity", "unit_price"}

class Metrics(TypedDict):
    total_revenue: float
    total_sold: int
    product_revenue: dict[str, float]
    best_product: str | None
    start_date: date | None
    end_date: date | None

def find_csv_files() -> list[Path]:
    """Return all CSV files in the input folder, sorted by filename."""
    return sorted(INPUT_FOLDER.glob("*.csv"))

def calculate_metrics(csv_files: list[Path]) -> Metrics:
    """Calculate sales metrics from the provided CSV files.

    Files missing required columns and rows containing invalid data are
    skipped rather than stopping the entire report.
    """
    metrics: Metrics = {
        "total_revenue": 0.0,
        "total_sold": 0,
        "product_revenue": {},
        "best_product": None,
        "start_date": None,
        "end_date": None
    }

    for csv_file in csv_files:
        with open(csv_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
                print(f"Skipping {csv_file}: missing required columns.")
                continue

            for row in reader:
                try:
                    quantity = int(row["quantity"])
                    unit_price = float(row["unit_price"])
                    product = (row["product"] or "").strip()
                    sale_date = date.fromisoformat(row["date"].strip())

                    if not product:
                        raise ValueError("Product name is empty.")

                    if quantity < 0 or unit_price < 0:
                        raise ValueError("Quantity and unit price cannot be negative.")

                    revenue = quantity * unit_price

                    metrics["total_revenue"] += revenue
                    metrics["total_sold"] += quantity

                    if product in metrics["product_revenue"]:
                        metrics["product_revenue"][product] += revenue
                    else:
                        metrics["product_revenue"][product] = revenue

                    if metrics["start_date"] is None or sale_date < metrics["start_date"]:
                        metrics["start_date"] = sale_date

                    if metrics["end_date"] is None or sale_date > metrics["end_date"]:
                        metrics["end_date"] = sale_date

                except (ValueError, TypeError, KeyError) as error:
                    print(f"Skipping invalid row: {row} ({error})")
                    continue

    # "Best product" is defined as the product with the highest total revenue.
    if metrics["product_revenue"]:
        metrics["best_product"] = max(
            metrics["product_revenue"],
            key=lambda product_name: metrics["product_revenue"][product_name]
        )

    return metrics

def write_report(metrics: Metrics) -> None:
    """Write the calculated sales metrics to output/report.csv."""
    if not metrics["product_revenue"]:
        print("No sales data found.")
        return

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    report_path = OUTPUT_FOLDER / "report.csv"

    with open(report_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])
        writer.writerow([
            "Report Timeframe",
            f"{metrics['start_date']} to {metrics['end_date']}"
        ])
        writer.writerow(["Total Revenue", f"{metrics['total_revenue']:.2f}"])
        writer.writerow(["Total Sold", metrics["total_sold"]])
        writer.writerow(["Best Product", metrics["best_product"]])

        writer.writerow([])
        writer.writerow(["Product", "Revenue"])

        for product, revenue in sorted(metrics["product_revenue"].items()):
            writer.writerow([product, f"{revenue:.2f}"])

    print("Report generated successfully.")

def main() -> None:
    csv_files = find_csv_files()
    if not csv_files:
        print("No csv files found in input folder.")
        return

    metrics = calculate_metrics(csv_files)
    write_report(metrics)

if __name__ == "__main__":
    main()