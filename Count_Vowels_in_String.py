# Problem Three: Create a function that counts the number of vowels and consonants within a given string
# This method should return a dictionary with two keys -  “vowels” and “consonants”, and values of the number of times each appears in the string
# spaces and numbers will not be ignored
# count = {vowels: {a:1, e:2 etc}, consonants: {b:2, c:4 etc.}}
# steps
#   decalare a vowels list ["a", "e", "o", "u"]
#   loop through the string
#   check if the char is alpha, if so make it lowercase
#   check if its vowel if it is, use the get function 
#   

        


def count_vowels_consonants(input_string: str)-> dict[str,dict[str,int]]:
    vowel_and_consonant_count = {"vowels":{"a":0, "e":0, "o":0, "i":0, "u":0}, "consonants":{}}
    for char in input_string:
        if char.isalpha():
            if char in vowel_and_consonant_count["vowels"]:
                vowel_and_consonant_count["vowels"][char] = vowel_and_consonant_count["vowels"][char] + 1
            else:
                vowel_and_consonant_count["consonants"][char] = vowel_and_consonant_count["consonants"].get(char,0) + 1
        else:
            continue
    return vowel_and_consonant_count

count_vowels_consonants("abc")