categories = [x for x in input().split(', ')]

n = int(input())

items_log = {x: [] for x in categories}
quantity_log = {x: 0 for x in categories}
qualtity_log = {x: 0 for x in categories}

for _ in range(n):
    command = input().split(' - ')
    category = command[0]
    item = command[1]
    qty_qua = command[2].split(';')
    split_qty = qty_qua[0].split(':')
    quantity = int(split_qty[1])
    split_qua = qty_qua[1].split(':')
    quality = int(split_qua[1])
    items_log[category].append(item)
    quantity_log[category] += quantity
    qualtity_log[category] += quality

print(f'Count of items: {sum(quantity_log.values())}')
print(f'Average quality: {sum(qualtity_log.values()) / len(qualtity_log):.2f}')
[print(f'{k} -> {", ".join(v)}') for k, v in items_log.items()]
