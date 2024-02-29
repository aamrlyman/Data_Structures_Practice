from Algorithms.prime_number_generator import crossOutMultiple, crossOutMultiples, primeNumberGenerator
import pytest

primeNumbersLessthan1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]

def createCrossOutMultipleOutPut(incrementer,limit):
    numDictList=[{"value":x,"isMultiple":False } for x in range(2,limit+1)]
    for dict in numDictList:
       if (dict["value"] == incrementer): continue
       if(dict['value'] % incrementer==0):
           dict["isMultiple"] = True
    return numDictList

def createCrossOutMulitplesTestCase(numberLimit):
    numDictList=[{"value":x,"isMultiple":True } for x in range(2,numberLimit+1)]
    for num in primeNumbersLessthan1000:
        if num > numberLimit: break;
        numDictList[num-2]["isMultiple"]=False
    return numDictList

@pytest.mark.parametrize("inputList,startingIndex,incrementer, outputList", 
    [([{"value":x,"isMultiple":False } for x in range(2,11)], 2, 2,createCrossOutMultipleOutPut(2,10)),
    ([{"value":x,"isMultiple":False } for x in range(2,11)], 4, 3, createCrossOutMultipleOutPut(3,10)), 
    ([{"value":x,"isMultiple":False } for x in range(2,51)], 12, 7, createCrossOutMultipleOutPut(7,50)), 
    ([{"value":x,"isMultiple":False } for x in range(2,101)], 12, 7, createCrossOutMultipleOutPut(7,100)), 
    ([{"value":x,"isMultiple":False } for x in range(2,101)], 24, 13, createCrossOutMultipleOutPut(13,100)), 
    ([{"value":x,"isMultiple":False } for x in range(2,3)], 2, 2, createCrossOutMultipleOutPut(2,2)), 
     
     ]
                         )
def test_crossOutMultiple(inputList, startingIndex, incrementer, outputList):
    crossOutMultiple(inputList, startingIndex, incrementer)
    assert inputList == outputList
@pytest.mark.parametrize("inputList,numberLimit, outputList", 
    [
        ([{"value":x,"isMultiple":False } for x in range(2,11)], 10, createCrossOutMulitplesTestCase(10)),
        ([{"value":x,"isMultiple":False } for x in range(2,51)], 50, createCrossOutMulitplesTestCase(50)),
        ([{"value":x,"isMultiple":False } for x in range(2,101)], 100, createCrossOutMulitplesTestCase(100)),
        ([{"value":x,"isMultiple":False } for x in range(2,1001)], 1000, createCrossOutMulitplesTestCase(1000)),
        ([{"value":x,"isMultiple":False } for x in range(2,3)], 2, createCrossOutMulitplesTestCase(2)),
        ([{"value":x,"isMultiple":False } for x in range(2,2)], 1, createCrossOutMulitplesTestCase(1)),
        ([{"value":x,"isMultiple":False } for x in range(2,198)], 197, createCrossOutMulitplesTestCase(197)),
     
     ]
                         )
def test_crossOutMultiples(inputList, numberLimit, outputList):
    crossOutMultiples(inputList,numberLimit)
    assert inputList == outputList
@pytest.mark.parametrize("numberLimit, correctOutputList", 
    [
        (10,[prime for prime in primeNumbersLessthan1000 if prime <= 10]),
        (100,[prime for prime in primeNumbersLessthan1000 if prime <= 100]),
        (50,[prime for prime in primeNumbersLessthan1000 if prime <= 50]),
        (47,[prime for prime in primeNumbersLessthan1000 if prime <= 47]),
        (1,[prime for prime in primeNumbersLessthan1000 if prime <= 1]),
        (0,[prime for prime in primeNumbersLessthan1000 if prime <= 0]),
        (1000,[prime for prime in primeNumbersLessthan1000 if prime <= 1000]),
     ]
                         )
def test_primeNumberGenerator(numberLimit, correctOutputList):
    assert primeNumberGenerator(numberLimit) == correctOutputList
