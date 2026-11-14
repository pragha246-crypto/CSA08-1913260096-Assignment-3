"""Command-line electricity bill calculator. Run: python src/electricity_billing.py"""
from decimal import Decimal
from tariff import generate_bill

def display_bill(bill: dict) -> str:
    lines = [
        "--------- ELECTRICITY BILL ---------",
        f"Consumer number : {bill['consumer_no']}",
        f"Consumer name   : {bill['consumer_name']}",
        f"Previous reading: {bill['previous_reading']} kWh",
        f"Current reading : {bill['current_reading']} kWh",
        f"Units consumed  : {bill['units']} units",
        f"Energy charge   : Rs. {bill['energy_charge']:.2f}",
        f"Fixed charge    : Rs. {bill['fixed_charge']:.2f}",
        f"Surcharge       : Rs. {bill['surcharge']:.2f}",
        "------------------------------------",
        f"TOTAL PAYABLE   : Rs. {bill['total_bill']:.2f}",
    ]
    return "\n".join(lines)

def main() -> None:
    print("ELECTRICITY BILL CALCULATOR")
    try:
        consumer_no = input("Consumer number: ").strip()
        consumer_name = input("Consumer name: ").strip()
        previous = int(input("Previous meter reading: "))
        current = int(input("Current meter reading: "))
        bill = generate_bill(consumer_no, consumer_name, previous, current)
        print(display_bill(bill))
    except (ValueError, TypeError) as exc:
        print(f"Input error: {exc}")

if __name__ == "__main__":
    main()
