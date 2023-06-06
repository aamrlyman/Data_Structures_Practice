# https://www.enjoyalgorithms.com/blog/application-of-stack-data-structure-in-programming

exp = "(1 + 2) * 3"


def Expression_Converter(expression):
    operators = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        ")": 0
    }
    stack = []
    postfix_expression = ""
    for x in expression:
        if x.isnumeric():
            postfix_expression += x
        elif x == "(":
            stack.append(x)
        elif x == ")":
            for operator in stack:
                if operator == "(":
                    stack.pop()
                    break
                else:
                    postfix_expression += stack.pop()
        else:
            for operator in stack:
                if operators[operator] >= x:
                    postfix_expression += stack.pop()
                stack.append(x)
    if len(stack) > 0:
        for operator in stack:
            postfix_expression += stack.pop()
    return postfix_expression

x = Expression_Converter(exp)
print(x)

print(type("100"))