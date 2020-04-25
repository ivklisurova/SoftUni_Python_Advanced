names = [x for x in input().split(', ')]

log_items = {i: [] for i in names}
log_cost = {i: 0 for i in names}


while True:
    command = input()
    if command == 'End':
        break
    command = command.split('-')
    name = command[0]
    item = command[1]
    cost = int(command[2])
    if item not in log_items[name]:
        log_items[name].append(item)
        log_cost[name] += cost

[print(f'{k} -> Items: {len(v)}, Cost: {log_cost[k]}') for k,v in log_items.items()]
