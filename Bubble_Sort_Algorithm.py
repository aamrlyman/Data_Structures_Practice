# Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.


num_list = [10,5,8,12,3,1]
num2_list = [50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9]

def sort_Algorithm(list):
    list_length = len(list)
    for index in range(list_length -1):
        num_one = list[index]
        num_two = list[index +1]
        if(num_one > num_two):
            list[index +1] = num_one
            list[index] = num_two
    print(list)  
    for index in range(list_length-1):
        num_1 = list[index]
        num_2 = list[index+1]
        if(num_1 > num_2):
            sort_Algorithm(list)
            break
    
    return list

sorted_list = sort_Algorithm(num2_list)
sorted_list2 = sort_Algorithm(num_list)

print(sorted_list)
# print(sorted_list2)