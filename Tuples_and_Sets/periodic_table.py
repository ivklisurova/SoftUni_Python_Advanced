n = int(input())

unique_compounds = set()

for _ in range(n):
    compounds = input().split(' ')
    [unique_compounds.add(i) for i in compounds]

[print(x) for x in unique_compounds]