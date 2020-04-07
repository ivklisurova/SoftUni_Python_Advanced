from collections import deque

litters = int(input())
queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue.append(command)

while queue:
    args = input()
    if args.startswith('refill'):
        args = args.split(' ')
        current_litters = int(args[1])
        litters += current_litters
    else:
        current_person = queue.popleft()
        if litters >= int(args):
            print(f'{current_person} got water')
            litters -= int(args)
        else:
            print(f'{current_person} must wait')


print(f'{litters} liters left')