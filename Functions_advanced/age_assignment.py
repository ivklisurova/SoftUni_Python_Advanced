def age_assignment(*args,**kwargs):
    result = {}
    for i in args:
        result[i] = 0
    for k,v in kwargs.items():
        for y in result:
            if y.startswith(k):
                result[y] = v
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
