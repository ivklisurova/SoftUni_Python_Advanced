text = tuple(input())

set_text = set(text)

ordered_list = list(sorted(set_text, key=lambda x: x))

[print(f'{i}: {text.count(i)} time/s') for i in ordered_list]
