present_count = int(input())
size = int(input())
matrix = []
dropped_presents = 0
total_count = 0
pos = []
my_dict = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
for i in range(size):
    line = input().split()
    matrix.append(line)
    for j in range(size):
        if line[j] == 'S':
            pos = [i, j]

while True:
    command = input()
    if command == 'Christmas morning':
        [print(' '.join(x)) for x in matrix]
        print(f'Good job, Santa! {dropped_presents} happy nice kid/s.')
        break
    change_dir = my_dict[command]
    new_row = pos[0] + change_dir[0]
    new_col = pos[1] + change_dir[1]
    if matrix[new_row][new_col] == 'X':
        matrix[pos[0]][pos[1]] = '-'
        pos = [new_row, new_col]
        matrix[pos[0]][pos[1]] = 'S'
    elif matrix[new_row][new_col] == 'V':

        matrix[pos[0]][pos[1]] = '-'
        pos = [new_row, new_col]
        matrix[pos[0]][pos[1]] = 'S'
        dropped_presents += 1

    elif matrix[new_row][new_col] == '-':
        matrix[pos[0]][pos[1]] = '-'
        pos = [new_row, new_col]
        matrix[pos[0]][pos[1]] = 'S'
    elif matrix[new_row][new_col] == 'C':
        matrix[pos[0]][pos[1]] = '-'
        pos = [new_row, new_col]
        matrix[pos[0]][pos[1]] = 'S'
        row = pos[0]
        col = pos[1]
        while present_count != total_count:
            if matrix[row - 1][col] in 'XV':
                total_count += 1
                dropped_presents += 1
                matrix[row - 1][col] = '-'
            if matrix[row + 1][col] in 'XV':
                total_count += 1
                dropped_presents += 1
                matrix[row + 1][col] = '-'
            if matrix[row][col - 1] in 'XV':
                total_count += 1
                dropped_presents += 1
                matrix[row][col - 1] = '-'
            if matrix[row][col + 1] in 'XV':
                total_count += 1
                dropped_presents += 1
                matrix[row][col + 1] = '-'
        print('Santa ran out of presents!')
        [print(' '.join(x)) for x in matrix]
        print(f'No presents for {dropped_presents} nice kid/s.')
        print(total_count)