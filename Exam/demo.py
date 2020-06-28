from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]
my_dict = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
crafts = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

win = False

while effects and casings:

    effect = effects.popleft()
    casing = casings.pop()
    total = effect + casing
    if total in my_dict.keys():
        bomb = my_dict[total]
        crafts[bomb] += 1
    else:
        effects.appendleft(effect)
        casings.append(casing - 5)
    if all(value >= 3 for value in crafts.values()):
        win = True
        break

if win:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in effects])}')
else:
    print(f'Bomb Effects: empty')
if casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in casings[::-1]])}')
else:
    print("Bomb Casings: empty")
for k, v in sorted(crafts.items()):
    print(f"{k}: {v}")