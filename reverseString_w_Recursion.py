def reverse_String(string:str):
    if len(string) == 0: 
        return string
    else: 
        temp = string[0]
        reverse_String(string[1:])

string = reverse_String("12345")
print(string)

def reverse1(string:str, index:int, n:int):
	if index == n: # return if we reached at last index or at the end of the string
		return
	temp = string[index] # storing each character starting from index 0 in function call stack;
	reverse(string, index+1, n) # type: ignore # calling recursive function by increasing index everytime
	print(temp, end="") # printing each stored character while recurring back

# Driver code
string = "Geeks for Geeks"
n = len(string)
reverse1(string, 0, n)

# This code is contributed by Potta Lokesh

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

string = "Geeks for Geeks"
reversed_string = reverse(string)
print(reversed_string)


def reverse_w_loop(string):
    l = []
    index = 0
    last_index = len(string)-1
    for char in string:
        l.append(string[last_index-index])
        index+=1
    return "".join(l)

print(reverse_w_loop("123456789"))
