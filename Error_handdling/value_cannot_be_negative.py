class ValueCannotBeNegative(Exception):
    """
    Returns exception if negative value is found

    """
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
    else:
        print('Positive')
