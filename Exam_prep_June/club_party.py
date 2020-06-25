from collections import deque

n = int(input())

reservations = input().split(' ')

halls = deque()
guests = []

current_status = 0

while reservations:
    args = reservations.pop()
    if args.isalpha():
        halls.append(args)
    else:
        if halls:
            current_status += int(args)
            if current_status > n:
                print(f'{halls.popleft()} -> {", ".join(guests)}')
                guests.clear()
                current_status = 0
                if halls:
                    current_status += int(args)
                    guests.append(args)
            else:
                guests.append(args)
