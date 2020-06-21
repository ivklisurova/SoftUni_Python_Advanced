from collections import deque

string = deque(input().split(' '))

main_colors = ['red', 'yellow', 'blue']

secondary_colors = {'orange': ('red', 'yellow'), 'purple': ('red', 'blue'), 'green': ('yellow', 'blue')}

collected_colors = []

while string:
    if len(string) == 1:
        variant = string.popleft()
        if variant in main_colors or variant in secondary_colors.keys():
            collected_colors.append(variant)
    else:
        first_substring = string.popleft()
        second_substring = string.pop()
        variant_one_color = first_substring + second_substring
        variant_two_color = second_substring + first_substring

        if variant_one_color in main_colors or variant_one_color in secondary_colors.keys():
            collected_colors.append(variant_one_color)
        elif variant_two_color in main_colors or variant_two_color in secondary_colors.keys():
            collected_colors.append(variant_two_color)
        else:
            middle_of_string = len(string) // 2
            cropped_first_substring = first_substring[:-1]
            cropped_second_substring = second_substring[:-1]
            if len(cropped_first_substring) > 0:
                string.insert(middle_of_string, cropped_first_substring)
            if len(cropped_second_substring) > 0:
                string.insert(middle_of_string, cropped_second_substring)

for i in collected_colors:
    if i in secondary_colors.keys():
        a = secondary_colors[i]
        for col in a:
            if col not in collected_colors:
                collected_colors.remove(i)

print(collected_colors)