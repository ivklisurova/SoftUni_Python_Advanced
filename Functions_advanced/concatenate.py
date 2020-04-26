def concatenate(*args):
    string = ''
    for i in args:
        string += i
    return string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
