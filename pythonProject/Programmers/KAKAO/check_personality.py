from collections import defaultdict


def change(problem, score):
    transform_dict = {"TR": "RT", "FC": "CF", "MJ": "JM", "AN": "NA"}
    if problem in transform_dict.keys():
        score = 4 - score
        problem = transform_dict[problem]
        return problem, score
    else:
        score = score - 4
        return problem, score


def solution(survey, choices):
    answer = ''
    pro = ["RT", "CF", "JM", "AN"]
    di = defaultdict(int)

    for p in pro:
        di[p]

    for idx, problem in enumerate(survey):
        p, s = change(problem, choices[idx])
        di[p] += s

    for i in range(4):
        if di[pro[i]] > 0:
            answer = answer + pro[i][0]
        else:
            answer = answer + pro[i][1]
    return answer
