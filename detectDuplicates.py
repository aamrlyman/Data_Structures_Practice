from collections import deque
import math
# Problem One: Create a function to detect and print duplicate characters from a given string
# BONUS: Modify the function to also include the number of times the duplicate character appears in the string

# Algorithm
# convert the string to a list
# bysect the string into single item lists that can be merged
# use a sort algorithm to merge the str
# create a string merge sort
# use a stack to check for duplicates
# use a stack to cuont the number of duplicates


def string_to_deque(string: str):
    return deque(string)

def merge(main: deque[str], left: deque[str], right: deque[str]) -> deque[str]:
    while (left and right):
        if (ord(left[0]) <= ord(right[0])):
            main.append(left.popleft())
        else:
            main.append(right.popleft())
    while (left):
        main.append(left.popleft())
    while (right):
        main.append(right.popleft())
    return main

def merge_Sort(array: deque[str]) -> deque[str]:
    if (len(array) < 2):
        return array
    array_length = len(array)
    l_array = deque()
    r_array = deque()
    for index in range(math.floor(array_length/2)):
        l_array.append(array.pop())
    for i in range(math.floor(array_length/2), array_length):
        r_array.append(array.pop())
    merge_Sort(l_array)
    merge_Sort(r_array)
    return merge(array, l_array, r_array)

def string_to_deque_and_Merge_Sort(string) -> deque[str]:
    return merge_Sort(string_to_deque(string))

def count_Sorted_Duplicates(array: deque[str]):
    currentChar = None
    duplicates = {}
    count = 0
    for char in array:
        if (currentChar == None):
            currentChar = char
        elif (currentChar == char):
            count += 1
        elif (currentChar != char and count > 0):
            duplicates[currentChar] = count
            count = 0
            currentChar = char
        else:
            currentChar = char
    return duplicates

def countDuplicates(string):
    return count_Sorted_Duplicates(string_to_deque_and_Merge_Sort(string))
# is this bad code writing because I am getting a type error?


# thing = count_Duplicates(deque(["a", "a", "b","c"]))
# print(thing)

def test(input: str, expected: dict):
    output = countDuplicates(input)
    status = "CORRECT" if output == expected else "FAILED"
    print(f'{status},input:{input}, output: {output}, expected: {expected}')


long_string = "https://app.reachreporting.com/login?_gl=1*xei3s6*_gcl_aw*R0NMLjE2NjE5ODA5NzkuQ2owS0NRandqYnlZQmhDZEFSSXNBQXJDNkxMNkZsY2s2OWxyZzRndHFvR0pYeGtydFRPajRqR3dPajVXWWg4VG92clpJZHBDZUtydzF5QWFBa0wzRUFMd193Y0I.*_ga*MTcxNTQzMjA2Mi4xNjU4ODUyOTgw*_ga_Y4YY4F094Q*MTY2MTk4MDk3OC4yNS4wLjE2NjE5ODA5NzguNjAuMC4w"
test("ZXXY", {"x":1})
test("gfedcbaa", {"a":1})
test(long_string,{})


def count_duplicates(input_string):
    char_count = {}
    for char in input_string:
        if char.isalnum() and char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

