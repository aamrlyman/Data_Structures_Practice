# Problem Five: Create a function that calculates the difference between a given number and 15.  If the difference is greater than 10, return double the absolute difference

def differenceComputation(num1:int, comparisonNum:int)-> int:
    diffNum = abs(num1 - comparisonNum)
    if (diffNum > 10 ):
        return diffNum*2
    else:
        return 0
    
print(differenceComputation(26,15))


def test(input1:int,input2:int, expected:int)->None:
    output = differenceComputation(input1,input2)
    status = "Correct" if output == expected else "INCORRECT"
    print(f'{status}, num1:{input1}, comparisonNum: {input2}, output:{output} expected: {expected}')


test(26,15, 22)
test(15,15, 0)
test(-15,15, 60)
test(100,15, 170)
test(-100,15, 230)
test(30,15, 30)
test(-30,15, 90)
