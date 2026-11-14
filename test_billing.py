import sys
import unittest
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tariff import calculate_units, calculate_energy_charge, generate_bill

class BillingTests(unittest.TestCase):
    def test_units(self):
        self.assertEqual(calculate_units(1250, 1390), 140)
    def test_zero_units_energy(self):
        self.assertEqual(calculate_energy_charge(0), Decimal("0.00"))
    def test_first_boundary(self):
        self.assertEqual(calculate_energy_charge(100), Decimal("150.00"))
    def test_one_above_first(self):
        self.assertEqual(calculate_energy_charge(101), Decimal("152.50"))
    def test_second_boundary(self):
        self.assertEqual(calculate_energy_charge(200), Decimal("400.00"))
    def test_one_above_second(self):
        self.assertEqual(calculate_energy_charge(201), Decimal("404.00"))
    def test_sample_bill(self):
        bill = generate_bill("D1024", "Arun Kumar", 1250, 1390)
        self.assertEqual(bill["total_bill"], Decimal("300.00"))
    def test_surcharge_boundary(self):
        self.assertEqual(generate_bill("X1", "Test", 0, 300)["surcharge"], Decimal("0.00"))
        self.assertEqual(generate_bill("X1", "Test", 0, 301)["surcharge"], Decimal("40.20"))
    def test_invalid_decreasing_reading(self):
        with self.assertRaises(ValueError):
            calculate_units(1200, 1100)
    def test_negative_reading(self):
        with self.assertRaises(ValueError):
            calculate_units(-1, 10)
    def test_blank_consumer(self):
        with self.assertRaises(ValueError):
            generate_bill("", "Name", 0, 10)

if __name__ == "__main__":
    unittest.main()
