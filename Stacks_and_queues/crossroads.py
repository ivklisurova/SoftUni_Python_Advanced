from collections import deque

queue = deque()

duration = int(input())
free_window = int(input())

passed_cars = 0

while True:
    args = input()
    left_duration = duration
    if args == 'END':
        print('Everyone is safe.')
        print(f'{passed_cars} total cars passed the crossroads.')
        break
    if args == 'green':
        while queue:
            current_car = queue.popleft()
            car = deque(current_car)
            for i in range(1, left_duration + 1):
                if car:
                    car.popleft()
                    if len(car) == 0:
                        passed_cars += 1
                        left_duration -= i
                        continue
            if len(car) > 0:
                for j in range(free_window):
                    car.popleft()
                    if len(car) == 0:
                        passed_cars += 1
                        break
                if len(car) > 0:
                    print('A crash happened!')
                    print(f'{current_car} was hit at {car[0]}.')
                    break
            break
    else:
        queue.append(args)
