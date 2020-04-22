from collections import deque

n, m = map(int, input().split(' '))

snake = deque(input())

matrix = []

for row in range(n):
    current_list = []
    for element in range(m):
        snake_part = snake.popleft()
        current_list.append(snake_part)
        snake.append(snake_part)
        if row % 2 != 0:
            if element == m-1:
                current_list = current_list[::-1]
    matrix.append(current_list)
    print(''.join(matrix[row]))
