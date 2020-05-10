def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for i in range(3, n + 1):
        new_row = []
        previous_row = triangle[-1]
        for j in range(i):
            if j == 0:
                new_row.append(previous_row[0])
            elif j == i-1:
                new_row.append(previous_row[-1])
            else:
                sum_new_position = previous_row[j-1]+previous_row[j]
                new_row.append(sum_new_position)
        triangle.append(new_row)

    return triangle




print(get_magic_triangle(7))
