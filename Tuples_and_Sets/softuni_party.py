guests = set()
reservations = set()

while True:
    reservation = input()
    if reservation == 'PARTY':
        break
    reservations.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break
    guests.add(guest)

diff = list(guests ^ reservations)
sorted_diff = sorted(diff, key=lambda x: x)
print(len(diff))

[print(i) for i in sorted_diff if i[0].isdigit()]
[print(j) for j in sorted_diff if j[0].isalpha()]
