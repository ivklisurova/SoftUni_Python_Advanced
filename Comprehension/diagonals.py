n = int(input())

matrix = [list(map(int,input().split(', '))) for i in range(n)]

first_diagonal = [matrix[row][row] for row in range(len(matrix))]

matrix = matrix[::-1]

second_diagonal = [matrix[row][row] for row in reversed(range(len(matrix)))]


print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}')