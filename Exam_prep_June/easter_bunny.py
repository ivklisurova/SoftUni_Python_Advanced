def locate_bunny(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                location = (r, c)
                return location


def solve(dirs, curr_loc, matrix):
    global max_sum
    global best_position
    current_sum = 0
    new_position = curr_loc
    bunny_eggs_loc = {}
    for k, v in dirs.items():
        while True:
            new_position = (new_position[0] + v[0], new_position[1] + v[1])
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(matrix) or new_position[1] >= len(
                    matrix[new_position[0]]):
                new_position = curr_loc
                if current_sum > max_sum:
                    max_sum = current_sum
                    current_sum = 0
                    best_position = k
                break
            if matrix[new_position[0]][new_position[1]] == 'X':
                new_position = curr_loc
                if current_sum > max_sum:
                    max_sum = current_sum
                    current_sum = 0
                    best_position = k
                break

            current_sum += int(matrix[new_position[0]][new_position[1]])
            if k not in bunny_eggs_loc:
                bunny_eggs_loc[k] = []
            bunny_eggs_loc[k].append([new_position[0], new_position[1]])
    return bunny_eggs_loc


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
n = int(input())

field = [input().split(' ') for i in range(n)]

max_sum = 0
best_position = None

bunny_location = locate_bunny(field)
eggs_positions = solve(directions, bunny_location, field)

print(best_position)

[print(x) for x in eggs_positions[best_position]]

print(max_sum)
