# Problem Nine: Create a function that will convert a given numeric value into the corresponding number of hours and minutes
# I will create a function that can take in a value in a given unit milliseconds, seconds, minutes, hours
# and return the value converted to a new unit with the new unit and converting any remainder values into smaller units.
# integers and decimals will be handled

from dataclasses import dataclass
from enum import Enum
class UnitName(Enum):
    hour = "hour"
    minute = "minute"
    second = "second"
    millisecond = "millisecond"


units: dict[UnitName, int] = {
    UnitName.hour: 3600000,
    UnitName.minute: 60000,
    UnitName.second: 1000,
    UnitName.millisecond: 1,
}


def formatOutPutString(outPutDict: dict[UnitName, int], negativeCase: str) -> str:
    outPutString = ""
    outPutList: list[str] = []
    for key, value in outPutDict.items():
        if (value > 0):
            plural_suffix = "s" if value > 1 else ""
            unitString = f'{value} {key.value}{plural_suffix}'
            outPutList.append(unitString)
    outPutListLength = len(outPutList)
    for index, string in enumerate(outPutList):
        puncuation = "," if (outPutListLength > 1 and index <
                             outPutListLength-1) else ""
        outPutString += f'{negativeCase}{string}{puncuation} '
    outPutString = outPutString.strip() if outPutString.strip() else "0"
    return outPutString

def unit_conversion(amount: int, inputUnit: UnitName, outputUnit: UnitName, units: dict[UnitName, int]) -> str:
    positiveOrNegativePrefix = ""
    if (amount < 0):
        amount = abs(amount)
        positiveOrNegativePrefix = "-"
    unitOrder = [x for x in units]
    outPutDict = {}
    convertingLargerUnitToSmallerUnit = True if (units[inputUnit] > units[outputUnit]) else False
    if(convertingLargerUnitToSmallerUnit):
        return f'{amount * units[inputUnit]//units[outputUnit]} {outputUnit.value}s'
    else:
        if (inputUnit.value != UnitName.millisecond):
            amount *= units[inputUnit]
        for index in range(unitOrder.index(outputUnit), len(unitOrder)):
            outPutDict[unitOrder[index]] = amount // units[unitOrder[index]]
            remainder = amount % units[unitOrder[index]]
            amount = remainder
    return formatOutPutString(outPutDict, positiveOrNegativePrefix)

set = {"a", "b","c"}
print(set)
tuple = (1,2,3,4)
for index in range(len(tuple)):
    print(index)
    print(tuple[index])