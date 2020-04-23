text = input().split(', ')

dictionary_comp = {key: ord(key) for key in text}

print(dictionary_comp)