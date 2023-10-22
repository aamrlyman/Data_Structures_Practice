# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).

# n log n complexity

list1 = ["bob", "joe", "sam", "bob"]
list2 = ["bob", "joe", "sam"]
list3 = ["1", "1"]
list4 = ["bob"]
list5 = []
list6 = [1,2,3]


def check_list_for_duplicates(list:list):
    if(not list):
        return False
    list.sort()
    name_Stack = list[0]
    for index in range(1, len(list)):
        name = list[index]
        if(name == name_Stack):
            return True
        name_Stack = name
    return False

print(check_list_for_duplicates(list1))        
print(check_list_for_duplicates(list2))        
print(check_list_for_duplicates(list3))        
print(check_list_for_duplicates(list4))        
print(check_list_for_duplicates(list5))        
print(check_list_for_duplicates(list6))        
