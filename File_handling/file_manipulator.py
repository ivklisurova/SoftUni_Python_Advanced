from os import remove, replace

while True:
    args = input()
    if args == 'End':
        break
    args = args.split('-')
    command = args[0]
    file_name = args[1]
    if command == 'Create':
        file = open(file_name, 'w')
    elif command == 'Add':
        content = args[2]
        file = open(file_name, 'a')
        file.write(f'{content}\n')
        file.close()
    elif command == 'Replace':
        old_string = args[2]
        new_string = args[3]
        with open(file_name, 'r')as file:
            file_data = file.read()
        new_data = file_data.replace(old_string, new_string)
        with open(file_name, 'w') as file:
            file.write(new_data)
    elif command == 'Delete':
        try:
            remove(file_name)
        except:
            print('An error occurred')
