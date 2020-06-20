def count_alive_cells(field):
    alive_cells = 0
    for j in field:
        for x in j:
            if x > 0:
                alive_cells += 1
    return alive_cells


def sum_alive_cells(field):
    total_sum = 0
    for j in field:
        for x in j:
            if x > 0:
                total_sum += x
    return total_sum


def is_in_field(field, new_cell_row, new_cell_col):
    valid = True
    # check row
    if new_cell_row < 0 or new_cell_row > len(field) - 1:
        valid = False
    # check col
    if new_cell_col < 0 or new_cell_col > len(field) - 1:
        valid = False
    return valid


def detonate_the_bomb(row, col, field, bomb):
    max_rows = [-1, 1, 0, 0, 1, -1, -1, 1]
    max_cols = [0, 0, 1, -1, 1, 1, -1, -1]

    for i in range(len(max_rows)):
        new_cell_row, new_cell_col = row + max_rows[i], col + max_cols[i]
        if is_in_field(field, new_cell_row, new_cell_col):
            if field[new_cell_row][new_cell_col] > 0:
                field[new_cell_row][new_cell_col] = field[new_cell_row][new_cell_col] - abs(bomb)

    return field


n = int(input())

field = [list(map(int, input().split(' '))) for _ in range(n)]
bombs = input().split(' ')
bomb_coordinates = [list(map(int, i.split(','))) for i in bombs]

for i in bomb_coordinates:
    row = i[0]
    col = i[1]
    # locate the bomb / power of the bomb
    bomb = field[row][col]
    # detonate the bomb
    detonate_the_bomb(row, col, field, bomb)
    # utilized bomb set to 0
    field[row][col] = 0

print(f'Alive cells: {count_alive_cells(field)}')
print(f'Sum: {sum_alive_cells(field)}')

for item in field:
    print(' '.join(str(x) for x in item))
