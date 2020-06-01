string_numbers = input().split('|')

matrix = [x.split() for x in string_numbers[::-1]]

flatten_list = [j for i in matrix for j in i]

print(' '.join(flatten_list))
