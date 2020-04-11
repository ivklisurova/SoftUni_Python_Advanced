n = int(input())

position = 0

for i in range(n):
    args = input().split(' ')
    petrol = int(args[0])
    distance = int(args[1])

    if petrol >= distance:
        position = i
        break

print(position)
