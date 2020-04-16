n = int(input())

usernames = set()

for _ in range(n):
    name = input()
    usernames.add(name)

[print(username) for username in usernames]
