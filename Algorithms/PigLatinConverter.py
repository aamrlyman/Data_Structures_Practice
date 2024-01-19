# Problem Six: Create a “Pig Latin Converter” function, that can translate a given string into Pig Latin
# English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word, and adding ‘ay’.  
# Word that start with a vowel just recieve the "ay" suffix
# EXAMPLE: “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”
# I Will capitalize the start of the sentence and remove any caps from the original string



def Pig_Latin_Converter(string:str) -> str:
        vowels:list[str] = ["a", "e", "i", "o", "u"]
        Lower_Case_String = string.lower()
        separated_words_list = Lower_Case_String.split()
        for word in separated_words_list:
            if(not word.isalpha()):
                raise Exception(f'{word} has non-alphabet characters')
        for index,word in enumerate(separated_words_list):
            if(len(word)<2 or word[0] in vowels):
                separated_words_list[index] = word+"ay"
            else:
                separated_words_list[index] = f'{word[1:len(word)]}{word[0]}ay'
        separated_words_list[0] = separated_words_list[0].capitalize()
        return " ".join(separated_words_list)

    
answer = Pig_Latin_Converter("The quick brown fox went around")

print(answer)