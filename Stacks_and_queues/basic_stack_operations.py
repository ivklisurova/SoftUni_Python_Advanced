n_s_x = input().split(' ')
elements = input().split(' ')

stack = []

n = int(n_s_x[0])
s = int(n_s_x[1])
x = n_s_x[2]

for i in range(n):
    stack.append(elements[i])

for y in range(s):
    stack.pop()

if len(stack)>0:
    if x in stack:
        print('True')

    else:
        print(min(stack))
else:
    print('0')

