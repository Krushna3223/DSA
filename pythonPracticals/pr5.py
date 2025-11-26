# Program: Infix to Postfix Conversion (Final Correct Version)

def precedence(ch):
    if ch == '^':
        return 3
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    else:
        return 0

stack = []
postfix = []

exp = input("Enter infix expression: ")

# Add '(' at beginning and ')' at end
exp = "(" + exp + ")"

for ch in exp:

    # Ignore spaces
    if ch == ' ':
        continue

    if ch.isalnum():   # operand (A, B, C or numbers)
        postfix.append(ch)

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()   # remove '(' safely

    else:  # operator
        while stack and precedence(ch) <= precedence(stack[-1]):
            postfix.append(stack.pop())
        stack.append(ch)

# Print result
print("Postfix expression is:", end=" ")
for i in postfix:
    print(i, end="")
print()

