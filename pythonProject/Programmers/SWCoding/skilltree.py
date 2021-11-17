# 스킬트리


def solution(skill, skill_trees):
    answer = 0

    for sk_tr in skill_trees:
        chk = list()

        for i in range(len(skill)):
            find_sk = skill[i]
            idx = sk_tr.find(find_sk)
            if idx == -1:
                chk.append(-1)
            else:
                chk.append(idx)
        if (chk_OK(chk)):
            answer += 1

    return answer


def chk_OK(chk):
    if chk.count(-1) == len(chk):
        return False
    if chk[0] == -1:
        return False
    for i in range(len(chk) - 1, 0, -1):
        term = 0
        if chk[i] == -1:
            term += 1
            continue
        if chk[i] > chk[i - 1]:
            if i - 1 == 0:
                return True
            continue
        else:
            return False


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))