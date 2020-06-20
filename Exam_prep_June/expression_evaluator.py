from collections import deque


def calculate(sign, result_list):
    final_result = result.popleft()
    while result_list:
        if sign == '*':
            final_result *= result_list.popleft()
        elif sign == '+':
            final_result += result_list.popleft()
        elif sign == '-':
            final_result -= result_list.popleft()
        elif sign == '/':
            final_result //= result_list.popleft()

    return final_result


string = input().split(' ')
result = deque()

for i in string:
    if i not in '*+-/':
        result.append(int(i))
    else:
        result.append(calculate(i, result))

[print(i) for i in result]