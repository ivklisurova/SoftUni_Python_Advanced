def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for i in args:
        result.append(i[0](*i[1]))
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
