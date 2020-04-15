parking_log = set()

while True:
    command = input()
    if command == 'END':
        break
    command = command.split(', ')
    direction, car_number = command[0], command[1]

    if direction == 'IN':
        parking_log.add(car_number)
    elif direction == 'OUT':
        parking_log.discard(car_number)

if parking_log:
    [print(i) for i in parking_log]
else:
    print(f'Parking Lot is Empty')