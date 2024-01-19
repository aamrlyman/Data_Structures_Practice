
def reassignedPriorities(priorities):
    stack = []
    minimizedPriorities = {}
    for priority in priorities:
        if priority not in stack:
            stack.append(priority)
    stack.sort()
    count = 1
    for item in stack:
        minimizedPriorities[item] = count
        count += 1
    for index, priority in enumerate(priorities):
        priorities[index] = minimizedPriorities[priority]
    return priorities
    


newPriorities = reassignedPriorities([1,8,4])
 
print(newPriorities)