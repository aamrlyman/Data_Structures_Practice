# Problem Nine: Create a function that will convert a given numeric value into the corresponding number of hours and minutes
# I will create a function that can take in a value in a given unit milliseconds, seconds, minutes, hours
# and return the value converted to a new unit with the new unit and converting any remainder values into smaller units. 
# integers and decimals will be handled

# steps 
# 
from dataclasses import dataclass
from enum import Enum

class UnitName(Enum):
    hour = "hour"
    minute = "minute"
    second = "second"
    millisecond = "millisecond" 


units: dict[UnitName,int] = {
    UnitName.hour: 3600000,
    UnitName.minute: 60000,
    UnitName.second: 1000,
    UnitName.millisecond: 1,
}

def unit_conversion(amount:int, inputUnit:UnitName, outputUnit:UnitName, units: dict[UnitName,int])->str:
    unitOrder = [x for x in units]
    outPutDict = {}
    outPutString = ""
    if(units[inputUnit] > units[outputUnit]): return f'{amount * units[inputUnit]//units[outputUnit]} {outputUnit.value}s'
    else: 
        for index in range(unitOrder.index(outputUnit), len(unitOrder)):
            outPutDict[unitOrder[index]] = amount // units[unitOrder[index]]
            remainder = amount % units[unitOrder[index]]
            amount = remainder
    for key,value in outPutDict.items():
        plural_suffix = "s" if value > 1 else ""
        # puncuation = "" if value == UnitName.millisecond else ", " 
        if(value > 0):
            outPutString+= f'{value} {key.value}{plural_suffix}'
    return outPutString

amount = unit_conversion(3600000, UnitName.millisecond, UnitName.hour, units)
print(amount)




# put all units in relation to the smallest baseline unit. Sort it apply the logic 
# name and relation to smallest unit 
# 0 hours 0 minutes 45 seconds ?? 

