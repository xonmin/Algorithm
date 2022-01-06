from collections import defaultdict


def solution(string):
    counting = defaultdict(int)

    for s in string:
        counting[s] += 1

    sorting_list = []

    for k, v in zip(counting.keys(), counting.values()):
        sorting_list.append([k, v])

    sorting_list.sort(key=lambda x: x[1],reverse=True)
    print(sorting_list)
    ans = [i[0] * i[1] for i in sorting_list]

    return "".join(ans)

print(solution("abcabaccsbscassa"))
