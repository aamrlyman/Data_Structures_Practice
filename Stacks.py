from collections import deque
# https://www.enjoyalgorithms.com/blog/application-of-stack-data-structure-in-programming
# are expressions usually represented as strings?
# What do you do about multi-digit numbers another for loop that adds all numbers to expression until an operator is reached?
# Handle spaces
# To convert the infix expression "1 + 2 * 3" to postfix notation, you can use the following steps:

# Create an empty stack to hold the operators temporarily.
# Initialize an empty string to store the postfix expression.
# Scan the expression from left to right.
# For each element in the expression, do the following:
# If it is an operand (a number), append it to the postfix expression.
# If it is an operator, do the following:
    # If the stack is empty or the top of the stack is an opening parenthesis, push the operator onto the stack.
    # If the operator has higher precedence than the top of the stack, push it onto the stack.
    # If the operator has lower or equal precedence to the top of the stack, pop operators from the stack and append them to the postfix expression until a lower precedence operator or an opening parenthesis is encountered. Then push the current operator onto the stack.
    # If the operator is a closing parenthesis, pop operators from the stack and append them to the postfix expression until an opening parenthesis is encountered. Discard the opening and closing parentheses.
    # After scanning the entire expression, pop any remaining operators from the stack and append them to the postfix expression.
# The postfix expression is the final output.
# Let's apply these steps to the given expression "1 + 2 * 3":

# Empty stack: []
# Empty postfix expression: ""
# Scanning "1 + 2 * 3" from left to right:

# 1: Operand, append to postfix expression: "1"
# +: Operator, stack is empty, push onto stack: ["+"]
# 2: Operand, append to postfix expression: "1 2"
# : Operator, stack is empty, push onto stack: ["", "+"]
# 3: Operand, append to postfix expression: "1 2 3"
# After scanning the entire expression, pop the remaining operators from the stack and append them to the postfix expression: "1 2 3 * +"

# Therefore, the postfix expression for "1 + 2 * 3" is "1 2 3 * +".
# https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html


exp = "1+2*3"
exp1 = "1+2*3"
exp2 = "1+2"
exp3 = "1*2"
exp4 = "1*2+3"


def Expression_Converter(expression):
    operators = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        ")": 0,
        "(": 0
    }
 
    stack = deque()
    postfix_expression = ""
    for x in expression: #(1+5)*(4+8)
        if x.isnumeric():
            postfix_expression += x
        elif x == ")":
            stack_length = len(stack)
            for index in range((stack_length - 1), -1, -1):
                while stack[index] == "(":
                    stack.pop()
                    break
                else:
                    postfix_expression += stack.pop()
        elif len(stack) == 0 or stack[-1] == "(" or operators[x] > operators [stack[-1]]:
            stack.append(x)
        elif operators[x] <= operators [stack[-1]]:
            postfix_expression+= stack.pop()
            stack.append(x)
    if len(stack) > 0:
        while len(stack) > 0:
            postfix_expression += stack.pop()
    return postfix_expression



exp = "1+2*3"
exp1 = "1+2*3"
exp2 = "1+2"
exp3 = "1*2"
exp4 = "1*2+3"

# print(Expression_Converter("1+5*4+8")) # 1 5 4 * + 8 +
# print(Expression_Converter("(1+5)*(4+8)")) # 1 5 + 4 8 + *
# print(Expression_Converter("1*5+4*8")) # 1 5 * 4 8 * +    CORRECT
# print(Expression_Converter("1+5+4+8")) # 1 5 + 4 + 8 +    CORRECT
# print(Expression_Converter("((1+5))+(4)+8")) # 1 5 + 4 + 8 +    NOT CORRECT
print(Expression_Converter("(1+5)*3+4+8")) # 15+3*4+8+    NOT CORRECT



