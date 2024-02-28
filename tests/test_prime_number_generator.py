from Algorithms.prime_number_generator import crossOutMultiple
import pytest

def createCorrectTestCase(incrementer,limit):
    numDictList=[{"value":x,"isMultiple":False } for x in range(2,limit+1)]
    for dict in numDictList:
       if (dict["value"] == incrementer): continue
       if(dict['value'] % incrementer==0):
           dict["isMultiple"] = True
    return numDictList

@pytest.mark.parametrize("inputList,startingIndex,incrementer, outputList", 
    [([{"value":x,"isMultiple":False } for x in range(2,11)], 2, 2,createCorrectTestCase(2,10)),
    ([{"value":x,"isMultiple":False } for x in range(2,11)], 4, 3, createCorrectTestCase(3,10)), 
    ([{"value":x,"isMultiple":False } for x in range(2,51)], 12, 7, createCorrectTestCase(7,50)), 
    ([{"value":x,"isMultiple":False } for x in range(2,101)], 12, 7, createCorrectTestCase(7,100)), 
    ([{"value":x,"isMultiple":False } for x in range(2,101)], 24, 13, createCorrectTestCase(13,100)), 
    ([{"value":x,"isMultiple":False } for x in range(2,3)], 2, 2, createCorrectTestCase(2,2)), 
     
     ]
                         )
def test_crossOutMultiple(inputList, startingIndex, incrementer, outputList):
    crossOutMultiple(inputList, startingIndex, incrementer)
    assert inputList == outputList
