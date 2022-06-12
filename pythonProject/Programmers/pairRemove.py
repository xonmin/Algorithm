def solution(s):
    temp = []
    for c in s:
        if len(temp) == 0:
            temp.append(c)
            continue
        if temp[-1] == c:
            temp.pop()
        else:
            temp.append(c)
    if len(temp) == 0:
        return 1
    else:
        return 0


print(solution("baabaa"))
print(solution("cdcd"))
