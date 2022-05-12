def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        or_operation = bin(num1 | num2)
        str_map = str(or_operation)[2:]
        str_map = str_map.replace('1', '#')
        str_map = str_map.replace('0', ' ')
        if len(str_map) < n:
            for i in range(n - len(str_map)):
                str_map = ' ' + str_map
        answer.append(str_map)

    return answer
