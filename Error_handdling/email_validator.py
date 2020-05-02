class MustContainAtSymbolError(Exception):
    """
    Raises exception if @ symbol is not found

    """

    def __init__(self):
        self.message = 'Email must contain @'

    def __str__(self):
        return self.message


class NameTooShortError(Exception):
    """
    Raises exception when the length of the name is less than 4 symbols

    """
    def __init__(self):
        self.message = 'Name must be more than 4 characters'

    def __str__(self):
        return self.message


class InvalidDomainError(Exception):
    """
    Raises exception when invalid domain is used

    """
    def __init__(self):
        self.message = 'Domain must be one of the following: .com, .bg, .org, .net'

    def __str__(self):
        return self.message


valid_domains = ('.com', '.bg', '.org', '.net')

while True:
    command = input()
    if command == 'End':
        break
    email = command
    if '@' not in email:
        raise MustContainAtSymbolError
    else:
        email = email.split('@')
        name = email[0]
        domain = email[1]
        if len(name) <= 4:
            raise NameTooShortError
        if not domain.endswith(valid_domains):
            raise InvalidDomainError
        else:
            print('Email is valid')

