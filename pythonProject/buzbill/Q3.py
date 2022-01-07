from itertools import combinations


def countTeams(skills, minPlayers, minLevel, maxLevel):
    # 적어도 세명이상을고용하고 싶은 10과 4 스킬레벨을 가진
    reform_skill = sorted(skills)

    # sk = []
    # for s in reform_skill:
    #     if s <= minLevel:
    #         continue
    #     sk.append(s)
    sk = [i for i in reform_skill if i >= minLevel]
    sk = [i for i in sk if i <= maxLevel]

    ans = 0
    if minPlayers > len(sk):
        return ans

    for i in range(minPlayers, len(sk) + 1):
        ans += (len(list(combinations(sk, i))))

    return ans


print(countTeams([248, 779, 392, 727, 561], 2, 360, 1000))
print(countTeams([4, 8, 5, 6], 1, 5, 7))