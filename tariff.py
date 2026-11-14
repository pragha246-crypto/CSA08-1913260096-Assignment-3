"""Tariff calculation functions for the educational electricity-billing project."""
from decimal import Decimal

RATE_FIRST_100 = Decimal("1.50")
RATE_NEXT_100 = Decimal("2.50")
RATE_ABOVE_200 = Decimal("4.00")
FIXED_CHARGE = Decimal("50.00")
SURCHARGE_RATE = Decimal("0.05")
SURCHARGE_THRESHOLD = 300

def calculate_units(previous_reading: int, current_reading: int) -> int:
    if not isinstance(previous_reading, int) or not isinstance(current_reading, int):
        raise TypeError("Meter readings must be integers.")
    if previous_reading < 0 or current_reading < 0:
        raise ValueError("Meter readings cannot be negative.")
    if current_reading < previous_reading:
        raise ValueError("Current reading cannot be less than previous reading.")
    return current_reading - previous_reading

def calculate_energy_charge(units: int) -> Decimal:
    if not isinstance(units, int):
        raise TypeError("Units must be an integer.")
    if units < 0:
        raise ValueError("Units cannot be negative.")
    first = min(units, 100)
    second = min(max(units - 100, 0), 100)
    above = max(units - 200, 0)
    return (Decimal(first) * RATE_FIRST_100
            + Decimal(second) * RATE_NEXT_100
            + Decimal(above) * RATE_ABOVE_200)

def calculate_surcharge(units: int, energy_charge: Decimal) -> Decimal:
    if units > SURCHARGE_THRESHOLD:
        return (energy_charge * SURCHARGE_RATE).quantize(Decimal("0.01"))
    return Decimal("0.00")

def generate_bill(consumer_no: str, consumer_name: str,
                  previous_reading: int, current_reading: int) -> dict:
    if not consumer_no.strip() or not consumer_name.strip():
        raise ValueError("Consumer number and name cannot be blank.")
    units = calculate_units(previous_reading, current_reading)
    energy = calculate_energy_charge(units)
    surcharge = calculate_surcharge(units, energy)
    total = energy + FIXED_CHARGE + surcharge
    return {
        "consumer_no": consumer_no.strip(),
        "consumer_name": consumer_name.strip(),
        "previous_reading": previous_reading,
        "current_reading": current_reading,
        "units": units,
        "energy_charge": energy,
        "fixed_charge": FIXED_CHARGE,
        "surcharge": surcharge,
        "total_bill": total,
    }
