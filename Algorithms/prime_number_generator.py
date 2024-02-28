#steps:
# 1. generate an list of dictionaries {value: 1, isMultiple:false} for whatever length is given
# 2. Get the max factor to check = square root of the list's length
# 3. Walk through the list and check change is multiple to true if it is a multiple 
# 4. Push list items with isMultiple=false into a lsit 
import math

exampleList = [
               {'value': 2, 'isMultiple': False}, 
               {'value': 3, 'isMultiple': False}, 
               {'value': 4, 'isMultiple': False}, 
               {'value': 5, 'isMultiple': False}, 
               {'value': 6, 'isMultiple': False}, 
               {'value': 7, 'isMultiple': False}, 
               {'value': 8, 'isMultiple': False}, 
               {'value': 9, 'isMultiple': False},
               {'value': 10, 'isMultiple': False}]

def crossOutMultiple(newList:list, startingIndex:int, incrementer:int):
    for i in range(startingIndex,len(newList),incrementer):
        newList[i]["isMultiple"] = True




def crossOutMultiples(newList:list, numberLimit:int)->None:
    multiples = [multiple for multiple in range(2,int(math.sqrt(numberLimit))+1)]
    for index,multiple in enumerate(multiples):
        if(newList[index]["isMultiple"] == True): continue



def primeNumberGenerator(numberLimit:int)->list[int]:
    if(numberLimit < 2): return [0]
    newList = [{"value":num, "isMultiple":False} for num in range(2, numberLimit+1)]
    crossOutMultiples(newList,numberLimit)
    return [x['value'] for x in newList if x["isMultiple"]==False]

# primseList = primeNumberGenerator(10)
# print(primseList)

print([{"value":x,"isMultiple":False } for x in range(2,11)])