def santa_position(matrix):
    for row in range(len(matrix)):
        if 'S' in matrix[row]:
            santa_position_row = row
            santa_position_col = matrix[row].index('S')
            santa_position_in_matrix = (santa_position_row, santa_position_col)
            return santa_position_in_matrix


def clear_old_position(row, col, matrix):
    matrix[row][col] = '-'


def solve(row, col, matrix):
    global nice_kids
    global presents_count
    if matrix[row][col] == 'X' and presents_count:
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'V' and presents_count:
        matrix[row][col] = 'S'
        presents_count -= 1
        nice_kids -= 1
    elif matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        if matrix[row - 1][col] == 'X' or matrix[row - 1][col] == 'V' and presents_count:
            matrix[row - 1][col] = '-'
            presents_count -= 1
            if matrix[row - 1][col] == 'V':
                nice_kids -= 1
        if matrix[row + 1][col] == 'X' or matrix[row + 1][col] == 'V' and presents_count:
            matrix[row + 1][col] = '-'
            presents_count -= 1
            if matrix[row + 1][col] == 'V':
                nice_kids -= 1
        if matrix[row][col - 1] == 'X' or matrix[row][col - 1] == 'V' and presents_count:
            matrix[row][col - 1] = '-'
            presents_count -= 1
            if matrix[row][col - 1] == 'V':
                nice_kids -= 1
        if matrix[row][col + 1] == 'X' or matrix[row][col + 1] == 'V' and presents_count:
            matrix[row][col + 1] = '-'
            presents_count -= 1
            if matrix[row][col + 1] == 'V':
                nice_kids -= 1
    elif matrix[row][col] == '-' and presents_count:
        matrix[row][col] = 'S'


def not_visited_nice_kids(matrix):
    counter_not_visited = 0
    for row in matrix:
        for i in row:
            if i == 'V':
                counter_not_visited += 1
    return counter_not_visited


presents_count = int(input())

n = int(input())

neighbourhood = [input().split(' ') for _ in range(n)]
total_nice_kids = not_visited_nice_kids(neighbourhood)
nice_kids = not_visited_nice_kids(neighbourhood)
is_successful = False

while presents_count > 0:
    command = input()

    position = santa_position(neighbourhood)
    santa_row = position[0]
    santa_col = position[1]

    if command == 'Christmas morning':
        break
    if command == 'up':
        clear_old_position(santa_row, santa_col, neighbourhood)
        solve(santa_row - 1, santa_col, neighbourhood)

    elif command == 'down':
        clear_old_position(santa_row, santa_col, neighbourhood)
        solve(santa_row + 1, santa_col, neighbourhood)

    elif command == 'left':
        clear_old_position(santa_row, santa_col, neighbourhood)
        solve(santa_row, santa_col - 1, neighbourhood)

    elif command == 'right':
        clear_old_position(santa_row, santa_col, neighbourhood)
        solve(santa_row, santa_col + 1, neighbourhood)

    if nice_kids == 0:
        is_successful = True
        break

if presents_count == 0 and nice_kids:
    print('Santa ran out of presents!')

[print(' '.join(i)) for i in neighbourhood]

if is_successful:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    count_nice_kids = not_visited_nice_kids(neighbourhood)
    print(f'No presents for {count_nice_kids} nice kid/s.')
