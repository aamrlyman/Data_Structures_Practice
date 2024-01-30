# Problem Eight: Create a function that calculates all possible permutations of a given string
# ab, ba, 
# abc acb bac bca cab cba
import math

def stringPermutations(string:str)->float:
    repeatedCharacterDict = {}
    denominator = 1
    for char in string:
        repeatedCharacterDict[char] = repeatedCharacterDict.get(char,0) + 1
    for repeatedChar,count in repeatedCharacterDict.items():
        denominator *= math.factorial(count)
    return math.factorial(len(string))/denominator


def string_permutations_recursion(stringLength:int)->int:
    if(stringLength==1): 
        return 1
    else:
        return string_permutations_recursion(stringLength-1)*stringLength;

def get_string_length_and_permutations(string:str):
    stringlength: int = len(string)
    return string_permutations_recursion(stringlength)

def string_permutations_forloop(string:str)->int:
    n = len(string)
    result = 1
    for index in range(n,0, -1):
        result *=index
    return result 


# empty string
# repeated characters?? 
# unusual charaters !@#$%^&&*())_
