# Problem Three: Create a function that counts the number of vowels and consonants within a given string
# This method should return a dictionary with two keys -  “vowels” and “consonants”, and values of the number of times each appears in the string
# spaces and numbers will not be ignored
# count = {vowels: {a:1, e:2 etc}, consonants: {b:2, c:4 etc.}}
# steps
#   decalare a vowels list ["a", "e", "o", "u"]
#   loop through the string
#   check if the char is alpha, if so maek it lowercase
#   check if its vowel if it is, use the get function 
#   

def count_vowels_consonants(input_string: str)-> dict[str,dict[str,int]]:
    vowel_and_consonant_count = {}
    vowels = ["a", "e", "o", "i", "u"]
    for char in input_string:
        if char.isalnum() and char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    return char_count