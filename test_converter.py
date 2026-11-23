import unittest
from converter import convert


class ConverterTests(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(convert("length", 1, "km", "m"), 1000)
        self.assertAlmostEqual(convert("length", 1, "mi", "km"), 1.609344)

    def test_weight(self):
        self.assertAlmostEqual(convert("weight", 1, "kg", "lb"), 2.20462, places=4)

    def test_temperature(self):
        self.assertAlmostEqual(convert("temperature", 100, "c", "f"), 212)
        self.assertAlmostEqual(convert("temperature", 0, "c", "k"), 273.15)

    def test_bad_unit(self):
        with self.assertRaises(ValueError):
            convert("length", 1, "xx", "m")


if __name__ == "__main__":
    unittest.main()
