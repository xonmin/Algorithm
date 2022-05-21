import string


def scoring(n, opt):
    if opt == 'S':
        return n
    elif opt == 'D':
        return n ** 2
    else:
        return n ** 3


def star(prev, now):
    return [prev * 2, now * 2]


def acha(now):
    return -now


def solution(dartResult):
    answer = 0

    result = dartResult.split(string.digits)
    prev, now = 0, 0
    for case in result:
        if case.find('*'):
            answer -= prev
            now = scoring(case[0], case[1])
            prev, now = star(prev, now)
            answer += prev + now
        elif case.find('#'):
            now = scoring(case[0], case[1])
            now = acha(now)
            answer += now
        else:
            now = scoring(case[0], case[1])
            answer += now
        prev = now

    return answer


print(solution(import string
import re


def scoring(n, opt):
    if opt == 'S':
        return n
    elif opt == 'D':
        return n ** 2
    else:
        return n ** 3


def star(prev, now):
    return [prev * 2, now * 2]


def acha(now):
    return -now


def solution(dartResult):
    answer = 0

    result = []
    prev, now = 0, 0
    item = ''
    dartResult = dartResult.replace('10', 'k')

    for i in range(len(dartResult)):
        if dartResult[i] in string.digits or dartResult[i] == 'k':
            result.append(item)
            item = ''
            item = item + dartResult[i]
        else:
            item += dartResult[i]
    result.append(item)
    result.remove('')

    for case in result:
        if '*' in case:
            answer -= prev
            if case[0] == 'k':
                now = scoring(10, case[1])
            else:
                now = scoring(int(case[0]), case[1])
            prev, now = star(prev, now)
            answer += prev + now
        elif '#' in case:
            if case[0] == 'k':
                now = scoring(10, case[1])
            else :
                now = scoring(int(case[0]), case[1])
            now = acha(now)
            answer += now
        else:
            if case[0] == 'k':
                now = scoring(10,case[1])
            else:
                now = scoring(int(case[0]), case[1])
            answer += now
        prev = now

    return answer


print(solution('1S2D*3T'))
print(solution('1D2S3T*'))
print(solution('1T2D3D#'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D2S#10S'))
'1S2D*3T'))