def get_nice_kids(matrix):
    count = 0
    for r in matrix:
        for c in r:
            if c == 'V':
                count += 1
    return count


def get_location(matrix):
    for row in range(len(matrix)):
        if 'S' in matrix[row]:
            location = (row, matrix[row].index('S'))
            return location


def solve(matrix, loc, old_loc, directions):
    global count_presents
    global visited_nice_kids
    if matrix[loc[0]][loc[1]] == 'X':
        matrix[loc[0]][loc[1]] = 'S'
        matrix[old_loc[0]][old_loc[1]] = '-'
    elif matrix[loc[0]][loc[1]] == 'V':
        matrix[loc[0]][loc[1]] = 'S'
        matrix[old_loc[0]][old_loc[1]] = '-'
        count_presents -= 1
        visited_nice_kids += 1
    elif matrix[loc[0]][loc[1]] == 'C':
        matrix[loc[0]][loc[1]] = 'S'
        matrix[old_loc[0]][old_loc[1]] = '-'
        for v in directions.values():
            position = (loc[0] + v[0], loc[1] + v[1])
            if matrix[position[0]][position[1]] in 'VX' and count_presents:
                count_presents -= 1
                if matrix[position[0]][position[1]] == 'V':
                    visited_nice_kids += 1
                matrix[position[0]][position[1]] = '-'
    elif matrix[loc[0]][loc[1]] == '-':
        matrix[loc[0]][loc[1]] = 'S'
        matrix[old_loc[0]][old_loc[1]] = '-'
    return matrix


count_presents = int(input())
n = int(input())

neighborhood = [input().split() for x in range(n)]

nice_kids = get_nice_kids(neighborhood)
visited_nice_kids = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == 'Christmas morning':
        break
    if count_presents == 0:
        break
    santa_location = get_location(neighborhood)
    new_location = (santa_location[0] + directions[command][0], santa_location[1] + directions[command][1])
    solve(neighborhood, new_location, santa_location, directions)
    if count_presents == 0 and nice_kids > visited_nice_kids:
        print('Santa ran out of presents!')
        break
    elif count_presents == 0:
        break

[print(' '.join(x)) for x in neighborhood]

if visited_nice_kids == nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - visited_nice_kids} nice kid/s.')
