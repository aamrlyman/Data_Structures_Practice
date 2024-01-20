from Algorithms.anagram_check import isAnagram
import pytest


@pytest.mark.parametrize("input_value1, input_value2, expected_output", 
    [("listen", "silent", True), 
     ("heart", "earth", True),
     ("spot", "stop", True),
     ("race", "care", True),
     ("post", "tops", True),
     ("night", "thing", True),
     ("act", "cat", True),
     ("debit card","bad credit", True),
     ("desserts","stressed", True),
     ("cinema", "iceman", True),
     ("cineasdfasdma", "iceman", False)
     ]
                         )
def test_isAnagram(input_value1, input_value2, expected_output):
    result = isAnagram(input_value1, input_value2)
    assert result == expected_output
