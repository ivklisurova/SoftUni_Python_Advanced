phonebook = {}

while True:
    command = input()
    if command == 'search':
        break
    name, number = command.split('-')
    if name not in phonebook:
        phonebook[name] = None
    phonebook[name] = number

while True:
    searched_name = input()
    if searched_name == 'stop':
        break
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
