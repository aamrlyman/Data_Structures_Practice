# https://www.geeksforgeeks.org/merge-sort/

def merge(Main_Array: list[int], Left_Array: list[int], Right_Array: list[int]):
    Main_Array_index = 0
    Left_Array_index = 0
    Right_Array_index = 0
    Left_Array_Length = len(Left_Array)
    Right_Array_Length = len(Right_Array)
    while (Left_Array_index < Left_Array_Length and Right_Array_index < Right_Array_Length):
        left_item = Left_Array[Left_Array_index]
        right_item = Right_Array[Right_Array_index]
        if (left_item <= right_item):
            Main_Array[Main_Array_index] = left_item
            Main_Array_index += 1
            Left_Array_index += 1
        else:
            Main_Array[Main_Array_index] = right_item
            Main_Array_index += 1
            Right_Array_index += 1
    while (Left_Array_index < Left_Array_Length):
        left_item = Left_Array[Left_Array_index]
        Main_Array[Main_Array_index] = left_item
        Left_Array_index += 1
    while (Right_Array_index < Right_Array_Length):
        right_item = Right_Array[Right_Array_index]
        Main_Array[Main_Array_index] = right_item
        Right_Array_index += 1
        Main_Array_index += 1
    return Main_Array


def test(Main_Array: list[int], Left_Array: list[int], Right_Array: list[int], expected: list[int]):
    output = merge(Main_Array, Left_Array, Right_Array)
    status = "CORRECT" if output == expected else "FAILED"
    print(status, Main_Array, Left_Array, Right_Array, expected) 


test([7, 6, 3, 4, 2, 1], [1, 2, 4], [3, 6, 7], [1, 2, 3, 4, 6, 7])
test([12, 234, 34, 453, 123, 214], [12, 34, 234], [123, 214, 453], [12,34,123,214,234,453])
test([4,3,2,1], [1, 2], [3,4], [1, 2, 3, 4])
