command = input()
numbers = list(map(int, input().split(' ')))

if command == 'Odd':
    odd_list = filter(lambda x: x % 2, numbers)
    print(sum(odd_list) * len(numbers))
elif command == 'Even':
    even_list = filter(lambda x: x % 2 == 0, numbers)
    print(sum(even_list) * len(numbers))
