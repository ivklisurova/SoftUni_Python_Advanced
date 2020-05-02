file_path = 'numbers.txt'

file = open(file_path, 'r')

sum = 0

for num in file:
    sum += int(num)

print(sum)
