def numbers_searching(*args):
    my_list = []
    max_num = max(*args)
    min_num = min(*args)
    for i in range(min_num,max_num+1):
        if i not in args:
            missing_number = i
            my_list.append(missing_number)
    s = set([x for x in args if args.count(x) > 1])
    duplicate = list(s)
    my_list.append(sorted(duplicate))
    return my_list

print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))