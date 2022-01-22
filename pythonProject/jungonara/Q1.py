def solution(vote):
    a = vote.count('A')
    b = vote.count('B')
    c = vote.count('C')

    total = len(vote)

    if c >= total // 2:
        return 'C'

    if a == b:
        return 'AB'

    if a > b:
        return 'A'
    else:
        return 'B'


print(solution("ABBCCCBBAB"))