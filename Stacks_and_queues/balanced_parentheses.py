text = input()

stack = []

is_balanced = True

for i in text:
    if i in '({[':
        stack.append(i)
    if i in ')}]':
        a = stack[-1]
        if len(stack) > 0:
            b = stack.pop()
            if i == ')' and b != '(':
                is_balanced = False
                break
            elif i == '}' and a != '{':
                is_balanced = False
                break
            elif i == ']' and a != '[':
                is_balanced = False
                break
        else:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:

    print('NO')
