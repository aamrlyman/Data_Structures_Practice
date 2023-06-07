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

exp = "(1+2)*3"
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
    stack = []
    postfix_expression = ""
    for x in expression:
        if x.isnumeric():
            postfix_expression += x
        elif x == "(":
            stack.append(x)
        elif x == ")":
            for operator in range((len(stack) - 1), 0, -1):
                if operator == "(":
                    stack.pop()
                    break
                else:
                    postfix_expression += stack.pop()
        elif len(stack) == 0:
            stack.append(x)
        else:
            for operator in stack:
                if operators[operator] >= operators[x]:
                    postfix_expression += stack.pop()
                stack.append(x)
                break
    if len(stack) > 0:
        for operator in stack:
            postfix_expression += stack.pop()
    return postfix_expression



print(Expression_Converter(exp))
print(Expression_Converter(exp1))
print(Expression_Converter(exp2))
print(Expression_Converter(exp3))
print(Expression_Converter(exp4))

