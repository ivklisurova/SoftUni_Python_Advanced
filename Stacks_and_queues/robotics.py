from collections import deque


def calculate_waiting_frame(ss, mm, hh, time):
    ss += time
    if ss == 60:
        ss = 0
        mm += 1
        if minutes == 60:
            hh += 1
            mm = 0
            if hours == 24:
                hh = 0
    time_stamp = (hh, mm, ss)
    return time_stamp


names = input().split(';')

robots_dict = {}

for i in names:
    k, v = i.split('-')
    if k not in robots_dict:
        robots_dict[k] = int(v)

robots = deque([i for i in robots_dict.keys()])

processing = {}

start_time = input().split(':')

hours = int(start_time[0])
minutes = int(start_time[1])
seconds = int(start_time[2])

items = deque()

while True:
    item = input()
    if item == 'End':
        break
    items.append(item)

while items:
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
            if hours == 24:
                hours = 0
    current_time_stamp = (hours, minutes, seconds)
    if len(processing) > 0:
        for robot, stamp in processing.items():
            if stamp == current_time_stamp:
                processing.pop(robot)
                robots.append(robot)
                break
    next_item = items.popleft()
    if robots:
        available_robot = robots.popleft()
        print(f'{available_robot} - {next_item} [{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}]')
        time_to_wait = calculate_waiting_frame(seconds, minutes, hours, robots_dict[available_robot])
        processing[available_robot] = time_to_wait
    else:
        items.append(next_item)
