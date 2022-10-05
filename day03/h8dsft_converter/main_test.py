import unittest

from main import Temperature


class TestTemperature(unittest.TestCase):
    def test_methods(self):
        t = Temperature("0", "Kelvin")
        self.assertEqual(t.Print("Celcius"), "-273.15 Celcius")
        self.assertEqual(t.ToCelcius(), "-273.15 Celcius")
        self.assertEqual(t.ToKelvin(), "0.00 Kelvin")
        self.assertEqual(t.ToFahrenheit(), "-459.67 Fahrenheit")

        t = Temperature("0", "Celcius")
        self.assertEqual(t.Print("Kelvin"), "273.15 Kelvin")
        self.assertEqual(t.ToCelcius(), "0.00 Celcius")
        self.assertEqual(t.ToKelvin(), "273.15 Kelvin")
        self.assertEqual(t.ToFahrenheit(), "32.00 Fahrenheit")

        t = Temperature("0", "Fahrenheit")
        self.assertEqual(t.Print("Celcius"), "-17.78 Celcius")
        self.assertEqual(t.ToCelcius(), "-17.78 Celcius")
        self.assertEqual(t.ToKelvin(), "255.37 Kelvin")
        self.assertEqual(t.ToFahrenheit(), "0.00 Fahrenheit")

if __name__ == '__main__':
    unittest.main()