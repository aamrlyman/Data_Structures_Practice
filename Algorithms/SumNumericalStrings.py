# Problem Four: Create a function that computes the total sum of all numerical values within a given string 
# I will assume that numberical values that don't have spaces between them are single numbers (12 = 12 not 1+2, but 1dklkns2 = 1+2)
# initiate an empty list[int] for the numbers to be added
# initiate a en empty list[str] for multi digit numbers 
# walk through the string check if its a number. If it is add it to the stack
# then start a new for loop that starts walking through string at the next character continuing to add number characters to the stack until a space or non number char is reached
# Then pop the int version of the string from the string stack and add to the int stack
# Sum the completed list

def Sum_Nums_In_String(string:str)-> int:
    string_nums_stack:list[str] = []
    int_list:list[int] = [0]
    last_index = len(string)-1
    index = 0
    while index <= (last_index):
        char = string[index]
        if(char.isnumeric()):
            string_nums_stack.append(char)
            index+=1
            while (index <= (last_index)) and string[index].isnumeric():
                    string_nums_stack[0]+=string[index]
                    index+=1
            int_list.append(int(string_nums_stack.pop()))
            index+=1
        else:
             index+=1
    return sum(int_list)

def test(input:str,expected:int)->None:
    output = Sum_Nums_In_String(input)
    status = "CORRECT" if output == expected else "Incorrect"
    print(f'{status},input: {input},output: {output}')

print("sdsdf")

test("1w22d2", 25)
test("abc", 0)
test("1", 1)
test("12", 12)
test("aaa12aaa@#$s200a1", 213)
