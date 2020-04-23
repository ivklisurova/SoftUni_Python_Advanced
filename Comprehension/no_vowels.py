vowels = {'a', 'o', 'u', 'e', 'i'}

text = input()
result = [x for x in text if x.lower() not in vowels]

print(''.join(result))
