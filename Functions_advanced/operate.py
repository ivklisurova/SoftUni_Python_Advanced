def operate(fargs, *args):
    result = 0
    for i in range(len(args)):
        if i == 0:
            result = args[i]
        else:
            if fargs == '+':
                result += args[i]
            # elif fargs == '-':
            #     result -= args[i]
            elif fargs == '*':
                result *= args[i]
            # elif fargs == '/':
            #     result /= args[i]
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
# print(operate('/', 15, 3))
# print(operate('-', 12, 2))
