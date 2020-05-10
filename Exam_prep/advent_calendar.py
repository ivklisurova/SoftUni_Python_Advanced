def fix_calendar(*args):
    loops = len(args[0])
    while loops > 0:
        for i in range(len(args[0])-1):
            if args[0][i] > args[0][i + 1]:
                args[0][i], args[0][i + 1] = args[0][i + 1], args[0][i]
        loops -= 1
    return args[0]


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
