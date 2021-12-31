from itertools import combinations


def solution(relation):
    kind = len(relation)

    attribute = len(relation[0])

    key_comb = []
    key_index_list = [i for i in range(attribute)]
    for i in range(1, attribute + 1):  # 후보키 조합 뽑기
        key_comb.extend(combinations(key_index_list, i))

    ans = []
    for i in key_comb:
        tmp = [tuple([row[key] for key in i]) for row in relation]
        if len(set(tmp)) == kind:
            chk = True

            for j in ans:
                if set(j).issubset(set(i)):
                    chk = False
                    break
            if chk:
                ans.append(i)

    return len(ans)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
