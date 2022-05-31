import string

count = 0


def delete_zero(s):
    global count
    count += s.count('0')
    return s.replace('0', '')


def transform_binary(s):
    length = len(s)
    return bin(length)[2:]


def solution(s):
    change_count = 0
    while s != '1':
        s = delete_zero(s)
        s = transform_binary(s)
        print(s)
        change_count += 1
    return [change_count, count]

print(solution("1111111"))