from itertools import permutations


def chk(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    per = list(permutations(user_id, len(banned_id)))

    candi_list = []

    for users in per:
        if chk(users, banned_id) is False:
            continue
        else:
            users = set(users)
            if users not in candi_list:
                candi_list.append(users)

    return len(candi_list)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
