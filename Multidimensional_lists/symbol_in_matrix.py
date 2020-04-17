n = int(input())

matrix = [list(input()) for _ in range(n)]

symbol = input()

is_in_list = False

for i in range(len(matrix)):
    if symbol in matrix[i]:
        print(f'({i}, {matrix[i].index(symbol)})')
        is_in_list = True
        break

if not is_in_list:
    print(f'{symbol} does not occur in the matrix')
