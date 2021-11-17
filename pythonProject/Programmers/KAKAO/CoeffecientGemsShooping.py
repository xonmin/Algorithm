def solution(gems):
    answer = []

    gem  = set(gems)
    left , right =  0,0
    result = []

    while left <= right <= len(gems):
        if set(gems[left:right]) == gem:
            result.append([left+1,right])
            left += 1
        else:
            right += 1

    for x, y in result:
        answer.append(y-x)

    return result[answer.index(min(answer))]



print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
