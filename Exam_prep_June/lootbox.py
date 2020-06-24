from collections import deque

first_box = deque([int(x) for x in input().split(' ')])
second_box = [int(x) for x in input().split(' ')]

collection = []

while True:
    if not first_box:
        print('First lootbox is empty')
        break
    if not second_box:
        print('Second lootbox is empty')
        break
    first_item = first_box[0]
    second_item = second_box[-1]
    current_sum = first_item + second_item
    if current_sum % 2 == 0:
        collection.append(current_sum)
        first_box.popleft()
        second_box.pop()
    else:
        first_box.append(second_box.pop())
total_sum = sum(collection)
if total_sum >= 100:
    print(f'Your loot was epic! Value: {total_sum}')
else:
    print(f'Your loot was poor... Value: {total_sum}')
