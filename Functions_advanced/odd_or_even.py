def solve(ll, initial_ll):
    return sum(ll) * len(initial_ll)


command = input()
numbers = list(map(int, input().split(' ')))

if command == 'Odd':
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(solve(odd_numbers, numbers))
elif command == 'Even':
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(solve(even_numbers, numbers))
