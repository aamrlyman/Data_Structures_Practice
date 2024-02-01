from Algorithms.string_permutations import stringPermutations, string_permutations_forloop, get_string_length_and_permutations
import pytest

@pytest.mark.parametrize("input_value, expected_output", [
    ("a", 1),
    ("aaaa", 1),
    ("aab", 3),
    ("aab", 3),
    ("aabc", 12),
    ("aaabc", 20),
    ("ab", 2),
    ("abc", 6),
    ("abcd", 24),
    ("abcde", 120),
    ("abcdefg", 5040),
    ("aaabbbc", 140),
    ("",1),
    ("!@#$%^&&*())",119750400),
])









def test_stringPermutations(input_value, expected_output):
    result = stringPermutations(input_value)
    assert result == expected_output

@pytest.mark.parametrize("input_value, expected_output", [
    ("a", 1),
    ("ab", 2),
    ("abc", 6),
    ("abcd", 24),
    ("abcde", 120),
    ("abcdefg", 5040),
])
def test_stringPermutations_forloop(input_value, expected_output):
    result = string_permutations_forloop(input_value)
    assert result == expected_output

@pytest.mark.parametrize("input_value, expected_output", [
    ("a", 1),
    ("ab", 2),
    ("abc", 6),
    ("abcd", 24),
    ("abcde", 120),
    ("abcdefg", 5040),
])
def test_stringPermutations_recursion(input_value, expected_output):
    result = get_string_length_and_permutations(input_value)
    assert result == expected_output
