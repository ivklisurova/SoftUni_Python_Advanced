def parse_input(string):
    return list(map(int, string.split(', ')))


n = int(input())

matrix = [parse_input(input()) for _ in range(n)]

flattered = [num for sublist in matrix for num in sublist]

print(flattered)