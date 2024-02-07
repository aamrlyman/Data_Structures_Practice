from Algorithms.TimeConverter import unit_conversion, UnitName, units
import pytest

@pytest.mark.parametrize("amount, inputUnit, outputUnit, units, expected_output", [
    (3600000, UnitName.millisecond, UnitName.hour, units,"1 hour"),
    (3800000, UnitName.millisecond, UnitName.hour, units,"1 hour, 3 minutes, 20 seconds"),
    (3800856, UnitName.millisecond, UnitName.hour, units,"1 hour, 3 minutes, 20 seconds, 856 milliseconds"),
    (1, UnitName.hour, UnitName.millisecond, units, "3600000 milliseconds"),
    (-125, UnitName.minute, UnitName.hour, units, "-2 hours, -5 minutes"),
    (125, UnitName.minute, UnitName.hour, units, "2 hours, 5 minutes"),
    (0, UnitName.minute, UnitName.hour, units, "0"),
    (500, UnitName.minute, UnitName.hour, units, "8 hours, 20 minutes"),
    (4600, UnitName.second, UnitName.hour, units, "1 hour, 16 minutes, 40 seconds"),
    (4600, UnitName.second, UnitName.minute, units, "76 minutes, 40 seconds"),
    (4600, UnitName.millisecond, UnitName.second, units, "4 seconds, 600 milliseconds"),
    
   
])

def test_unit_conversion(amount, inputUnit, outputUnit, units, expected_output):
    result = unit_conversion(amount, inputUnit, outputUnit, units)
    assert result == expected_output

