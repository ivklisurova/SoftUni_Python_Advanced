def get_repeating_DNA(string):
    repeated_strings = []
    for i in range(len(string)):
        sub_str = string[i:i+10]
        string_slice = string[i+1:]
        if len(sub_str) == 10:
            if sub_str in string_slice:
                if sub_str not in repeated_strings:
                    repeated_strings.append(sub_str)
    return repeated_strings


test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)