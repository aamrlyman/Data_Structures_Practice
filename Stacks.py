# https://www.enjoyalgorithms.com/blog/application-of-stack-data-structure-in-programming
# are expressions usually represented as strings?
# What do you do about multi-digit numbers another for loop that adds all numbers to expression until an operator is reached?
# spaces 

exp = "(1+2)*3"


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
            for operator in range((len(stack) -1), 0, -1):
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

x = Expression_Converter(exp)
print(x)

print(type("100"))

