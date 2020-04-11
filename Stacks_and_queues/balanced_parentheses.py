text = input()

stack = []

is_balanced = None

for i in text:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    if i == ')' or i == '}' or i == ']':
        a = stack.pop()
        if i == ')' and a == '(':
            if is_balanced == False:
                break
            else:
                is_balanced = True
        elif i == '}' and a == '{':
            if is_balanced == False:
                break
            is_balanced = True
        elif i == ']' and a == '[':
            if is_balanced == False:
                break
        else:
            is_balanced = False

if is_balanced:
    print('YES')
else:

    print('NO')