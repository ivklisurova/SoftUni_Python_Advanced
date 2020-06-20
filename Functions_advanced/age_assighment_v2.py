def age_assignment(*args, **kwargs):
    age_log = {}
    for i in args:
        if i not in age_log:
            age_log[i] = 0
            for k, v in kwargs.items():
                if k == i[0]:
                    age_log[i] = v
    return age_log


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
