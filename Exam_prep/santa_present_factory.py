from collections import deque

boxes = list(map(int, input().split(' ')))
magic = deque(map(int, input().split(' ')))

presents = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
created_presents = []
couple_one = {'Doll', 'Wooden train'}
couple_two = {'Teddy bear', 'Bicycle'}

is_completed = False

while len(boxes) > 0 and len(magic) > 0:
    m = magic[0]
    b = boxes[-1]
    if m == 0 or b == 0:
        if m == 0:
            magic.popleft()
        if b == 0:
            boxes.pop()
        continue
    magic_level = m * b

    if magic_level < 0:
        sum_values = m + b
        boxes.pop()
        magic.popleft()
        boxes.append(sum_values)
        continue

    for k, v in presents.items():
        if magic_level == v:
            created_presents.append(k)
            boxes.pop()
            magic.popleft()
            is_completed = True

    if not is_completed:
        magic.popleft()
        curr_box = boxes.pop()
        boxes.append(curr_box + 15)

    is_completed = False

set_presents = set([x for x in created_presents])

if couple_one.issubset(set_presents) or couple_two.issubset(set_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if len(boxes) > 0:
    print(f'Materials left: {", ".join([str(x) for x in boxes[::-1]])}')
if len(magic) > 0:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')

final_presents_count = {}

for item in created_presents:
    if item not in final_presents_count:
        final_presents_count[item] = created_presents.count(item)

sorted_final_presents_count = dict(sorted(final_presents_count.items(), key=lambda x: x[0]))

[print(f'{k}: {v}') for k, v in sorted_final_presents_count.items()]
