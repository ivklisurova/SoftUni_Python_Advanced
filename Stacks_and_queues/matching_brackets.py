text = input()

stack = []

for i in range(len(text)):
    if text[i] == '(':
        stack.append(i)
    elif text[i] == ')':
        opening_idx = stack.pop()
        expression = text[opening_idx:i + 1]
        print(expression)
