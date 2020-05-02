names = input().split(' ')

sorted_names = list(sorted(names,key=lambda x: x,reverse=True))

print(' '.join(sorted_names))