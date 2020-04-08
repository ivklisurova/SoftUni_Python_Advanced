n = int(input())

stack = []

for _ in range(n):
    args = [int(x) for x in input().split(' ')]
    msg_type = args[0]
    if msg_type == 1:
        element = args[1]
        stack.append(element)
    if stack:
        if msg_type == 2:
            stack.pop()
        elif msg_type == 3:
            print(max(stack))
        elif msg_type == 4:
            print(min(stack))


print(', '.join([str(x) for x in stack[::-1]]))
