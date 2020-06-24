def find_strongest_eggs(*args):
    eggs_log = args[0]
    number_sublists = args[1]
    sublists = [eggs_log[i::number_sublists] for i in range(number_sublists)]

    strongest_eggs = []

    for sub_list in range(len(sublists)):
        middle_of_sequence = len(sublists[sub_list]) // 2
        the_egg = sublists[sub_list][middle_of_sequence]
        left_egg = sublists[sub_list][middle_of_sequence - 1]
        right_egg = sublists[sub_list][middle_of_sequence + 1]
        if the_egg > right_egg and the_egg > left_egg:
            if right_egg > left_egg:
                strongest_eggs.append(the_egg)

    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
