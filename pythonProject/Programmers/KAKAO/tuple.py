import re


def solution(s):
    answer = []
    result = set()
    change = s[2:-2].split('},{')

    change.sort(key=lambda x: len(x))

    for ele in change:
        tmp = set(list(map(int,ele.split(','))))

        diff = set.difference(tmp,result)

        answer += list(diff)
        result = tmp

    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution("{{20,111},{111}}"))
