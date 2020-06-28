from collections import deque


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


bomb_effect = deque(map(int, input().split(', ')))
bomb_casing = list(map(int, input().split(', ')))

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

pouch = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

win = False

while bomb_effect and bomb_casing:
    effect = bomb_effect[0]
    casing = bomb_casing[-1]
    result = effect + casing
    if result in bombs.values():
        key = get_key(result, bombs)
        pouch[key] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
        if all(value >= 3 for value in pouch.values()):
            win = True
            break
    else:
        bomb_casing[-1] -= 5

if win:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if bomb_effect:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effect])}')
else:
    print('Bomb Effects: empty')

if bomb_casing:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casing[::-1]])}')
else:
    print('Bomb Casings: empty')


for k, v in sorted(pouch.items()):
    print(f'{k}: {v}')
