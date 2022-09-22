from collections import defaultdict


def solution(people, limit):
    weight_dict = defaultdict(int)
    people, answer = sorted(people), 0
    for h in people:
        weight_dict[h] += 1

    for i in range(len(people), -1, -1):
        if weight_dict[people[i]] == 0:
            continue
        remain = limit - people[i]
        weight_dict[people[i]] -= 1
        passenger = max([w for x in list(weight_dict.keys()) if x <= remain])
        weight_dict[passenger] -= 1
        answer += 1

    return answer
