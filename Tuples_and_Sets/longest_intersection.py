n = int(input())

longest_intersection_len = 0
longest_intersection = ""

for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = map(int, first.split(','))
    second_start, second_end = map(int, second.split(','))

    first_set = set(i for i in range(first_start, first_end + 1))
    second_set = set(i for i in range(second_start, second_end + 1))

    intersection = first_set.intersection(second_set)
    length = len(intersection)

    if length > longest_intersection_len:
        longest_intersection_len = length
        longest_intersection = list(intersection)

print(f'Longest intersection is {longest_intersection} with length {longest_intersection_len}')
