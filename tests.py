import unittest
import conversions
import conversions_refactored


# This class will hold my tests for the temperature conversion functions.
class ConversionTests(unittest.TestCase):

    # This test will check Celsius to Kelvin conversions.
    def test_convertCelsiusToKelvin(self):
        print("Testing Celsius to Kelvin conversion for 0.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0.0), 273.15, places=2)

        print("Testing Celsius to Kelvin conversion for 100.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100.0), 373.15, places=2)

        print("Testing Celsius to Kelvin conversion for -273.15 C")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-273.15), 0.0, places=2)

        print("Testing Celsius to Kelvin conversion for 300.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(300.0), 573.15, places=2)

        print("Testing Celsius to Kelvin conversion for 25.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(25.0), 298.15, places=2)

    # This test will check Celsius to Fahrenheit conversions.
    def test_convertCelsiusToFahrenheit(self):
        print("Testing Celsius to Fahrenheit conversion for 0.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0.0), 32.0, places=2)

        print("Testing Celsius to Fahrenheit conversion for 100.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(100.0), 212.0, places=2)

        print("Testing Celsius to Fahrenheit conversion for -40.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-40.0), -40.0, places=2)

        print("Testing Celsius to Fahrenheit conversion for 300.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(300.0), 572.0, places=2)

        print("Testing Celsius to Fahrenheit conversion for 25.0 C")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(25.0), 77.0, places=2)

    # This test will check Fahrenheit to Celsius conversions.
    def test_convertFahrenheitToCelsius(self):
        print("Testing Fahrenheit to Celsius conversion for 32.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(32.0), 0.0, places=2)

        print("Testing Fahrenheit to Celsius conversion for 212.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(212.0), 100.0, places=2)

        print("Testing Fahrenheit to Celsius conversion for -40.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-40.0), -40.0, places=2)

        print("Testing Fahrenheit to Celsius conversion for 572.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(572.0), 300.0, places=2)

        print("Testing Fahrenheit to Celsius conversion for 77.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(77.0), 25.0, places=2)

    # This test will check Fahrenheit to Kelvin conversions.
    def test_convertFahrenheitToKelvin(self):
        print("Testing Fahrenheit to Kelvin conversion for 32.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(32.0), 273.15, places=2)

        print("Testing Fahrenheit to Kelvin conversion for 212.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(212.0), 373.15, places=2)

        print("Testing Fahrenheit to Kelvin conversion for -459.67 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-459.67), 0.0, places=2)

        print("Testing Fahrenheit to Kelvin conversion for 572.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(572.0), 573.15, places=2)

        print("Testing Fahrenheit to Kelvin conversion for 77.0 F")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(77.0), 298.15, places=2)

    # This test will check Kelvin to Celsius conversions.
    def test_convertKelvinToCelsius(self):
        print("Testing Kelvin to Celsius conversion for 273.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(273.15), 0.0, places=2)

        print("Testing Kelvin to Celsius conversion for 373.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(373.15), 100.0, places=2)

        print("Testing Kelvin to Celsius conversion for 0.0 K")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(0.0), -273.15, places=2)

        print("Testing Kelvin to Celsius conversion for 573.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(573.15), 300.0, places=2)

        print("Testing Kelvin to Celsius conversion for 298.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(298.15), 25.0, places=2)

    # This test will check Kelvin to Fahrenheit conversions.
    def test_convertKelvinToFahrenheit(self):
        print("Testing Kelvin to Fahrenheit conversion for 273.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(273.15), 32.0, places=2)

        print("Testing Kelvin to Fahrenheit conversion for 373.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(373.15), 212.0, places=2)

        print("Testing Kelvin to Fahrenheit conversion for 0.0 K")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(0.0), -459.67, places=2)

        print("Testing Kelvin to Fahrenheit conversion for 573.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(573.15), 572.0, places=2)

        print("Testing Kelvin to Fahrenheit conversion for 298.15 K")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(298.15), 77.0, places=2)


# This class will hold my tests for the refactored conversion function.
class RefactoredConversionTests(unittest.TestCase):

    # This test will check all temperature conversions in the refactored file.
    def test_convert_temperature_units(self):
        print("Testing refactored conversion from Celsius to Kelvin")
        self.assertAlmostEqual(conversions_refactored.convert("celsius", "kelvin", 0.0), 273.15, places=2)

        print("Testing refactored conversion from Celsius to Fahrenheit")
        self.assertAlmostEqual(conversions_refactored.convert("celsius", "fahrenheit", 100.0), 212.0, places=2)

        print("Testing refactored conversion from Fahrenheit to Celsius")
        self.assertAlmostEqual(conversions_refactored.convert("fahrenheit", "celsius", 32.0), 0.0, places=2)

        print("Testing refactored conversion from Fahrenheit to Kelvin")
        self.assertAlmostEqual(conversions_refactored.convert("fahrenheit", "kelvin", 77.0), 298.15, places=2)

        print("Testing refactored conversion from Kelvin to Celsius")
        self.assertAlmostEqual(conversions_refactored.convert("kelvin", "celsius", 273.15), 0.0, places=2)

        print("Testing refactored conversion from Kelvin to Fahrenheit")
        self.assertAlmostEqual(conversions_refactored.convert("kelvin", "fahrenheit", 373.15), 212.0, places=2)

    # This test will check all distance conversions in the refactored file.
    def test_convert_distance_units(self):
        print("Testing refactored conversion from miles to yards")
        self.assertAlmostEqual(conversions_refactored.convert("miles", "yards", 1.0), 1760.0, places=2)

        print("Testing refactored conversion from yards to miles")
        self.assertAlmostEqual(conversions_refactored.convert("yards", "miles", 1760.0), 1.0, places=2)

        print("Testing refactored conversion from miles to meters")
        self.assertAlmostEqual(conversions_refactored.convert("miles", "meters", 1.0), 1609.34, places=2)

        print("Testing refactored conversion from meters to miles")
        self.assertAlmostEqual(conversions_refactored.convert("meters", "miles", 1609.34), 1.0, places=2)

        print("Testing refactored conversion from yards to meters")
        self.assertAlmostEqual(conversions_refactored.convert("yards", "meters", 1.0), 0.91, places=2)

        print("Testing refactored conversion from meters to yards")
        self.assertAlmostEqual(conversions_refactored.convert("meters", "yards", 0.9144), 1.0, places=2)

    # This test will check converting a unit to itself.
    def test_convert_same_unit(self):
        print("Testing same unit conversion for Celsius")
        self.assertAlmostEqual(conversions_refactored.convert("celsius", "celsius", 25.0), 25.0, places=2)

        print("Testing same unit conversion for Fahrenheit")
        self.assertAlmostEqual(conversions_refactored.convert("fahrenheit", "fahrenheit", 77.0), 77.0, places=2)

        print("Testing same unit conversion for Kelvin")
        self.assertAlmostEqual(conversions_refactored.convert("kelvin", "kelvin", 300.0), 300.0, places=2)

        print("Testing same unit conversion for Miles")
        self.assertAlmostEqual(conversions_refactored.convert("miles", "miles", 2.0), 2.0, places=2)

        print("Testing same unit conversion for Yards")
        self.assertAlmostEqual(conversions_refactored.convert("yards", "yards", 10.0), 10.0, places=2)

        print("Testing same unit conversion for Meters")
        self.assertAlmostEqual(conversions_refactored.convert("meters", "meters", 5.0), 5.0, places=2)

    # This test will check incompatible unit conversions.
    def test_incompatible_units(self):
        print("Testing incompatible conversion from Celsius to Meters")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert("celsius", "meters", 10.0)

        print("Testing incompatible conversion from Miles to Kelvin")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert("miles", "kelvin", 5.0)

        print("Testing incompatible conversion from Yards to Fahrenheit")
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert("yards", "fahrenheit", 3.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
