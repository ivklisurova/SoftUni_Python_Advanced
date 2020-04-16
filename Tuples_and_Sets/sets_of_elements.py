n, m = map(int,input().split(' '))

n_set = set()
m_set = set()

for _ in range(n):
    n_number = int(input())
    n_set.add(n_number)

for _ in range(m):
    m_number = int(input())
    m_set.add(m_number)

final_set = n_set.intersection(m_set)

[print(x) for x in final_set]