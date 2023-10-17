from Count_Vowels_in_String import count_vowels_consonants
import pytest

@pytest.mark.parametrize("input_value, expected_output", [
    ("aaasaf", {"vowels":{"a":4, "e":0, "o":0, "i":0, "u":0}, "consonants":{"s":1,"f":1}}),
    ("abc", {"vowels":{"a":1, "e":0, "o":0, "i":0, "u":0}, "consonants":{"b":1,"c":1}}),
    ("adfg", {"vowels":{"a":1, "e":0, "o":0, "i":0, "u":0}, "consonants":{"d":1,"f":1, "g":1}}),
    ("@#$%", {"vowels":{"a":0, "e":0, "o":0, "i":0, "u":0}, "consonants":{}}),
    ("123aaa", {"vowels":{"a":3, "e":0, "o":0, "i":0, "u":0}, "consonants":{}}),

])
def test_count_vowels_consonants(input_value, expected_output):
    result = count_vowels_consonants(input_value)
    
    assert result["vowels"] == expected_output["vowels"]
    assert result["consonants"] == expected_output["consonants"]






