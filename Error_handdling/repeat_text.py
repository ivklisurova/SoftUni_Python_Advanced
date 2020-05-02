try:
    result = input() * int(input())
    print(result)
except ValueError:
    print('Variable times must be an integer')


