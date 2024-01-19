# Problem Seven: Create a function that will return the largest numeric value within a given list

def getMaxListValue(numList:list[int]) -> int:
    stack = [numList[0]]
    for index,num in enumerate(numList):
        if index == 0: continue
        if num > stack[0]: 
            stack.pop()
            stack.append(num)
    return stack[0]

nums = [123,4,56456]

maxNum = getMaxListValue(nums)

print(maxNum)

maxValue = max([num for num in nums])

print(max(nums))