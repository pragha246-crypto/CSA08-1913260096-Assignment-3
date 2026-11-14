# Task-to-code map

| Report task | Repository evidence |
|---|---|
| 1. Problem and data identification | README, sample_consumers.csv, tariff.py |
| 2. Values and data types | tariff.py uses str, int, Decimal, bool-like conditions |
| 3. Variables and constants | Named constants in tariff.py |
| 4. Expressions and calculations | calculate_units(), calculate_energy_charge(), calculate_surcharge() |
| 5. Input and conversion | electricity_billing.py converts meter readings to int and validates them |
| 6. Functions | Reusable functions in tariff.py and display_bill() |
| 7. Modules | tariff.py imported by electricity_billing.py |
| 8. Algorithm planning | Calculation sequence documented in README and report |
| 9. Implementation and testing | CLI program and tests/test_billing.py |
| 10. Expected versus actual | expected_results.csv and captured test output |
| 11. Design justification | Decimal currency, constants, functions, and dictionary bill record |
| 12. Adaptation | Report discusses revised rates/categories/decimal readings/ten-day bonus; extensions need separate implementation if required |
