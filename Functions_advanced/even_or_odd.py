def even_odd(*args):
    result = []
    if args[-1] == 'even':
        result = [args[i] for i in range(len(args)-1) if args[i] % 2 == 0]
    elif args[-1] == 'odd':
        result = [args[i] for i in range(len(args) - 1) if args[i] % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


############
# def even_odd(*args):
#     x = 0 if args[-1] == 'even' else 1
#     return [num for num in args[:-1] if num % 2 == x ]