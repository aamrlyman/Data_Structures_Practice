# Problem Four: Create a function that computes the total sum of all numerical values within a given string 
# I will assume that numberical values that don't have spaces between them are single numbers (12 = 12 not 1+2, but 1dklkns2 = 1+2)
# I will handle negative numnbers
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
        if(char == "-" and string[index+1].isnumeric()):
            string_nums_stack.append(char)
            index+=1 
        elif(char.isnumeric()):
            string_nums_stack.append(char)
            index+=1
            while (index <= (last_index)) and string[index].isnumeric():
                    next_Char = string[index]
                    string_nums_stack.append(next_Char)
                    index+=1
            int_list.append(int("".join(string_nums_stack)))
            string_nums_stack.clear()
            index+=1
        else:
            index+=1
    return sum(int_list)

