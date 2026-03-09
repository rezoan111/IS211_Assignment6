# This function will convert Celsius to Kelvin.
def convertCelsiusToKelvin(celsius):
    return celsius + 273.15


# This function will convert Celsius to Fahrenheit.
def convertCelsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# This function will convert Fahrenheit to Celsius.
def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# This function will convert Fahrenheit to Kelvin.
def convertFahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


# This function will convert Kelvin to Celsius.
def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15


# This function will convert Kelvin to Fahrenheit.
def convertKelvinToFahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32
