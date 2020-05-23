from collections import deque

names = input().split(';')

robots_names = deque()
robots_time = deque()

for i in names:
    k, v = i.split('-')
    robots_names.append(k)
    robots_time.append(int(v))

start_time = input().split(':')
hours_to_sec = int(start_time[0]) * 3600
minutes_to_sec = int(start_time[1]) * 60
seconds_to_sec = int(start_time[2])

current_time_sec = hours_to_sec + minutes_to_sec + seconds_to_sec

processing = {}

items = deque()

while True:
    item = input()
    if item == 'End':
        break
    items.append(item)

while items:
    current_time_sec += 1
    if len(processing) > 0:
        for robot, stamp in processing.items():
            rob_time, time_to_wt = stamp[0], stamp[1]
            if time_to_wt == current_time_sec:
                processing.pop(robot)
                robots_names.append(robot)
                robots_time.append(rob_time)
                break
    next_item = items.popleft()
    if robots_names:
        available_robot = robots_names.popleft()
        robot_time = robots_time.popleft()
        hh = current_time_sec // 3600
        mm = (current_time_sec % 3600) // 60
        ss = current_time_sec % 60
        print(f'{available_robot} - {next_item} [{hh:02d}:{mm:02d}:{ss:02d}]')
        time_to_wait = current_time_sec + robot_time
        processing[available_robot] = [robot_time, time_to_wait]
    else:
        items.append(next_item)
