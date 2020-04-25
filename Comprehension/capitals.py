country = [x for x in input().split(', ')]
capitals = [x for x in input().split(', ')]

couples = dict(zip(country, capitals))

[print(f'{k} -> {v}') for k, v in couples.items()]
