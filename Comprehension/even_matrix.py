def parse_input(string):
    return list(map(int, string.split(', ')))


n = int(input())

matrix = [parse_input(input()) for _ in range(n)]

even_mtrx = [[j for j in i if j % 2 == 0] for i in matrix]

print(even_mtrx)