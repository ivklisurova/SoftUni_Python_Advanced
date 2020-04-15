n = int(input())

s = []

for i in range(n):
    name = input()
    s.append(name)

for person in set(s):
    print(person)
