def solve(stack):
    reversed_stack = []
    while stack:
        a = stack.pop()
        reversed_stack.append(a)

    return ' '.join(reversed_stack)


n = input().split(' ')

print(solve(n))
