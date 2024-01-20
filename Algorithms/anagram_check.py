def string_to_dict(string:str)->dict[str,int]:
    stringDict = {}
    for char in string:
        if(stringDict.get(char)): stringDict[char]+=1
        else: stringDict.get(char,1)
    return stringDict

def isAnagram(string1:str, string2:str) ->bool:
    if len(string1) != len(string2): return False
    else:
        return string_to_dict(string1) == string_to_dict(string2)

print(isAnagram("abc", "acb"))
