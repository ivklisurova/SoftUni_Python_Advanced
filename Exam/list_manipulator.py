def list_manipulator(numbers, *args):
    result = None
    command = args[0]
    location = args[1]
    additional_numbers = list(args[2::])
    if command == 'add':
        if location == 'beginning':
            result = additional_numbers + numbers
        elif location == 'end':
            result = numbers + additional_numbers
    elif command == 'remove':
        if location == 'beginning':
            if additional_numbers:
                result = numbers[additional_numbers[0]:]
            else:
                result = numbers[1::]
        elif location == 'end':
            if additional_numbers:
                result = numbers[:-additional_numbers[0]]
            else:
                result = numbers[:-1]
    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
