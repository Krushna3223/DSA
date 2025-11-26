# Practical 4: Postfix Expression Evaluation

stack = []

expression = input("Enter a postfix expression (space separated): ")
exp = expression.split()     # split by space

for x in exp:

    # if operand → push into stack
    if x.isnumeric():
        stack.append(int(x))

    else:   # operator
        op2 = stack.pop()
        op1 = stack.pop()

        if x == '+':
            res = op1 + op2
        elif x == '-':
            res = op1 - op2
        elif x == '*':
            res = op1 * op2
        elif x == '/':
            res = op1 / op2

        stack.append(res)

print("Result =", stack.pop())
