text = input().split(', ')

comp = [f'{text[i]} -> {len(text[i])}' for i in range(len(text))]

print(', '.join(comp))