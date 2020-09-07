from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))

total_time = 0

is_accomplished = True

while customers:
    if not taxis and customers:
        is_accomplished = False
        break
    cust = customers[0]
    taxi = taxis[-1]
    if taxi >= cust:
        total_time += cust
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not is_accomplished:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

