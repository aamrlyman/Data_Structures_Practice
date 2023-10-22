from Algorithms.SumNumericalStrings import Sum_Nums_In_String
import pytest


@pytest.mark.parametrize("input_value, expected_output", [
    ("12", 12),
    ("1sdfs2", 3),
    ("1sd22fs2", 25),
    ("1", 1),
    ("0", 0),
    ("aaa12aaa@#$s200a1", 213),
    ("a-12a200a1", 189),
    ("a-12-a200a1", 189),
    ("--a-12-a200a1", 189),
])
def test_Sum_Nums_In_String(input_value, expected_output):
    result = Sum_Nums_In_String(input_value)
    assert result == expected_output






