phonebook = {}

while True:
    command = input()
    if command.isdigit():
        break
    name, number = command.split('-')
    if name not in phonebook:
        phonebook[name] = None
    phonebook[name] = number

n = int(command)

for _ in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
