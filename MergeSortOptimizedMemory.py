import math
from collections import deque

def merge(Main_Array: deque[int], Left_Array: deque[int], Right_Array: deque[int]):
    while (Left_Array and Right_Array):
        if (Left_Array[0] <= Right_Array[0]):
            Main_Array.append(Left_Array.popleft())
        else:
            Main_Array.append(Right_Array.popleft())
    while (Left_Array):
        Main_Array.append(Left_Array.popleft())
    while (Right_Array):
        Main_Array.append(Right_Array.popleft())
    return Main_Array


def merge_Sort(array):
    if (len(array) < 2):
        return array
    array_length = len(array)
    l_array = deque()
    r_array = deque()
    for index in range(math.floor(array_length/2)):
        r_array.append(array.pop())
    for i in range(math.floor((array_length/2)), array_length):
        l_array.append(array.pop())
    merge_Sort(l_array)
    merge_Sort(r_array)
    return merge(array, l_array, r_array)

def convert_to_deque(array: list[int]):
    opt_array = deque()
    while(array):
        opt_array.append(array.pop())
    print(opt_array)
    return opt_array

def convert_to_deque_and_Merge_Sort(array):
    return merge_Sort(convert_to_deque(array))

def test_merge_Sort(input: list[int], expected: deque[int]):
    output = convert_to_deque_and_Merge_Sort(input)
    status = "CORRECT" if output == expected else "FAILED"
    print(f'{status},input:{input}, output: {output}, expected: {expected}')


long_list = [749, 220, 95, 80, 159, 416, 514, 414, 681, 299, 198, 567, 950, 289, 438, 15, 130, 926, 702, 907, 440, 256, 175, 861, 225, 2, 597, 964, 845, 643, 58, 772, 706, 625, 625, 208, 876, 201, 647, 649, 735, 595, 187, 465, 548, 371, 145, 900, 220, 433, 559, 479, 61, 188, 396, 46, 708, 50, 378, 686, 515, 857, 706, 561, 154, 238, 853, 987, 146, 10, 556, 307, 196, 880, 437, 796, 745, 233, 284, 420, 35, 648, 578, 287, 675, 110, 595, 543, 885, 379, 833, 490, 621, 943, 31, 700, 463, 444, 930, 216, 324, 52, 457, 793, 579, 221, 771, 129, 709, 157, 22, 804, 945, 686, 994, 186, 350, 749, 365, 755, 397, 772, 87, 356, 115, 15, 844, 398, 909, 428, 606, 664, 552, 481, 696, 710, 946, 66, 759, 9, 1, 998, 502, 239, 654, 756, 303, 662, 100,
             686, 846, 18, 906, 517, 821, 350, 533, 945, 633, 972, 698, 865, 978, 226, 383, 5, 614, 424, 543, 554, 928, 524, 360, 171, 208, 700, 432, 294, 721, 260, 97, 650, 57, 815, 638, 754, 548, 787, 284, 52, 532, 335, 415, 415, 237, 707, 393, 392, 593, 921, 54, 818, 522, 685, 38, 471, 948, 302, 153, 477, 698, 903, 323, 803, 613, 240, 290, 107, 981, 886, 917, 629, 941, 314, 952, 854, 102, 342, 693, 70, 263, 864, 174, 369, 910, 669, 529, 682, 61, 562, 581, 245, 9, 116, 442, 924, 626, 533, 591, 6, 62, 606, 825, 352, 295, 744, 621, 94, 218, 834, 693, 659, 414, 163, 489, 347, 23, 363, 347, 736, 843, 341, 980, 988, 793, 81, 362, 104, 934, 69, 415, 86, 181, 569, 987, 778, 761, 861, 39, 478, 788, 711, 286, 791, 137, 689, 376, 723, 846, 356]
sorted_list = deque([1, 2, 5, 6, 9, 9, 10, 15, 15, 18, 22, 23, 31, 35, 38, 39, 46, 50, 52, 52, 54, 57, 58, 61, 61, 62, 66, 69, 70, 80, 81, 86, 87, 94, 95, 97, 100, 102, 104, 107, 110, 115, 116, 129, 130, 137, 145, 146, 153, 154, 157, 159, 163, 171, 174, 175, 181, 186, 187, 188, 196, 198, 201, 208, 208, 216, 218, 220, 220, 221, 225, 226, 233, 237, 238, 239, 240, 245, 256, 260, 263, 284, 284, 286, 287, 289, 290, 294, 295, 299, 302, 303, 307, 314, 323, 324, 335, 341, 342, 347, 347, 350, 350, 352, 356, 356, 360, 362, 363, 365, 369, 371, 376, 378, 379, 383, 392, 393, 396, 397, 398, 414, 414, 415, 415, 415, 416, 420, 424, 428, 432, 433, 437, 438, 440, 442, 444, 457, 463, 465, 471, 477, 478, 479, 481, 489, 490, 502, 514, 515, 517, 522, 524,
               529, 532, 533, 533, 543, 543, 548, 548, 552, 554, 556, 559, 561, 562, 567, 569, 578, 579, 581, 591, 593, 595, 595, 597, 606, 606, 613, 614, 621, 621, 625, 625, 626, 629, 633, 638, 643, 647, 648, 649, 650, 654, 659, 662, 664, 669, 675, 681, 682, 685, 686, 686, 686, 689, 693, 693, 696, 698, 698, 700, 700, 702, 706, 706, 707, 708, 709, 710, 711, 721, 723, 735, 736, 744, 745, 749, 749, 754, 755, 756, 759, 761, 771, 772, 772, 778, 787, 788, 791, 793, 793, 796, 803, 804, 815, 818, 821, 825, 833, 834, 843, 844, 845, 846, 846, 853, 854, 857, 861, 861, 864, 865, 876, 880, 885, 886, 900, 903, 906, 907, 909, 910, 917, 921, 924, 926, 928, 930, 934, 941, 943, 945, 945, 946, 948, 950, 952, 964, 972, 978, 980, 981, 987, 987, 988, 994, 998])
test_merge_Sort([7, 6, 3, 4, 2, 1, 5], deque([1, 2, 3, 4, 5, 6, 7]))
test_merge_Sort([-7, 6, 23, 54, 2, 1], deque([-7, 1, 2, 6, 23, 54]))
test_merge_Sort([4, 3, 2, 1], deque([1, 2, 3, 4]))
test_merge_Sort([4, 3, 2, 1, 0, -1, 23], deque([-1, 0, 1, 2, 3, 4, 23]))
test_merge_Sort(long_list, sorted_list)



#Questions: 
# 1) is there a way to always pull from the back and come out on top
# 2) If your indeces are ordered, use a hashmap. Reindex if you run out of integers for your max. No reason to reindex every time. 
# Not sure how those work under the hood in python, so id think that gives a penalty of an extra cpu instruction for every retrieval. 
# Though, id think that would make up for it vs reindexing every time. So your average retrieval time should be more predictable.
# You could also allocate a larger slice of memory than your max array and increment your “view” by one as you pop the first item. 
# Though im not convinced this will be better than a hashmap in terms of number of instructions for the indirection.
# Also were talking about python here so who knows.
# 3) I don't even know where to start with fixed length lists. 
# 4) Are dictionaries a hashmap under the hood?


# test_merge([12, 234, 34, 453, 123, 214], [12, 34, 234], [123, 214, 453], [12,34,123,214,234,453])
# test_merge([4,3,2,1], [1, 2], [3,4], [1, 2, 3, 4])
# test_merge([7, 6, 3, 4, 2, 1], [1, 2, 4], [3, 6, 7], [1, 2, 3, 4, 6, 7])
# test_merge([-4,3,-2,-1], [-2, -1], [-4,3], [-4,-2,-1,3])


# Generate a list of 300 random numbers
# random_numbers = [random.randint(1, 1000) for _ in range(300)]

# print(random_numbers)

# Keep memory linear. See if you can only double the memory. N not N log N. No more than one additional array that is no bigger than the starting one.
# Heap sort
# Cannot allocate more memory than the initial array requires. You don't create another array.  May not be possible without significantly increasing time complexity.

