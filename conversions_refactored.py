# This exception will be used for incompatible unit conversions.
class ConversionNotPossible(Exception):
    pass


# This function will convert one unit to another unit.
def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    # This dictionary groups the units by type.
    unit_types = {
        "celsius": "temperature",
        "fahrenheit": "temperature",
        "kelvin": "temperature",
        "miles": "distance",
        "yards": "distance",
        "meters": "distance"
    }

    # If the units are not valid, raise an exception.
    if fromUnit not in unit_types or toUnit not in unit_types:
        raise ConversionNotPossible

    # If the units are different types, raise an exception.
    if unit_types[fromUnit] != unit_types[toUnit]:
        raise ConversionNotPossible

    # If both units are the same, return the value.
    if fromUnit == toUnit:
        return float(value)

    # Temperature conversions will use Kelvin as the base unit.
    if unit_types[fromUnit] == "temperature":
        if fromUnit == "celsius":
            base_value = value + 273.15
        elif fromUnit == "fahrenheit":
            base_value = (value - 32) * 5 / 9 + 273.15
        else:
            base_value = value

        if toUnit == "celsius":
            return base_value - 273.15
        elif toUnit == "fahrenheit":
            return (base_value - 273.15) * 9 / 5 + 32
        else:
            return float(base_value)

    # Distance conversions will use Miles as the base unit.
    if fromUnit == "miles":
        base_value = value
    elif fromUnit == "yards":
        base_value = value / 1760
    else:
        base_value = value / 1609.34

    if toUnit == "miles":
        return float(base_value)
    elif toUnit == "yards":
        return base_value * 1760
    else:
        return base_value * 1609.34
