#steps:
# 1. generate an list of dictionaries {value: 1, isMultiple:false} for whatever length is given
# 2. Get the max factor to check = square root of the list's length
# 3. Walk through the list and check change is multiple to true if it is a multiple 
# 4. Push list items with isMultiple=false into a lsit 
import math



def primeNumberGenerator(numberLimit:int)->list[int]:
    if(numberLimit < 2): return []
    newList = [{"value":num, "isMultiple":False} for num in range(2, numberLimit+1)]
    crossOutMultiples(newList,numberLimit)
    return [x['value'] for x in newList if x["isMultiple"]==False]

def crossOutMultiples(newList:list, numberLimit:int):
    multiples = [multiple for multiple in range(2,int(math.sqrt(numberLimit))+1)] # Math rule: you don't need to check multiples larger than the numberlimit's square root
    for index,multiple in enumerate(multiples):
        if(newList[index]["isMultiple"] == True): continue
        startingIndex = (multiple * 2 ) - 2 # multiple by 2--we don't want to cross out the starting multiple, minus 2 because list[0] == 2
        crossOutMultiple(newList, startingIndex, multiple)

def crossOutMultiple(newList:list, startingIndex:int, incrementer:int):
    for i in range(startingIndex,len(newList),incrementer):
        newList[i]["isMultiple"] = True
