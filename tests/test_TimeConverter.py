from Algorithms.TimeConverter import unit_conversion, UnitName, units
import pytest

@pytest.mark.parametrize("amount, inputUnit, outputUnit, units, expected_output", [
    (3600000, UnitName.millisecond, UnitName.hour, units,"1 hour"),
    (1, UnitName.hour, UnitName.millisecond, units, "3600000 milliseconds"),
   
])

def test_unit_conversion(amount, inputUnit, outputUnit, units, expected_output):
    result = unit_conversion(amount, inputUnit, outputUnit, units)
    assert result == expected_output

