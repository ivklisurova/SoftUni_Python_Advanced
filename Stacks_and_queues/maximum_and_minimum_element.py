n = int(input())

stack = []

for i in range(n):
    args = input().split(' ')
    msg_type = args[0]
    if msg_type == '1':
        element = int(args[1])
        stack.append(element)
    elif msg_type == '2':
        if len(stack) > 0:
            stack.pop()
    elif msg_type == '3':
        print(max(stack))
    elif msg_type == '4':
        print(min(stack))

for j in range(len(stack) - 1):
    print(stack.pop(), end=', ')
print(stack.pop())
