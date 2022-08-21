class Person:
    value, score = -1, 0
    parent, child = None, []

    def __init__(self, value, parent):
        self.value = value
        self.score = 0
        self.parent = parent

        if parent is not None:
            parent.child.append(self)
            if parent.parent is not None:
                if parent.parent.parent is not None:
                    parent.parent.parent.score += 1
                parent.parent.score += 3
            parent.score += 10


def solution(invitation_pair):
    length = len(invitation_pair)
    invite_member = {}
    p, c = invitation_pair[0]

    first = Person(p, None)
    second = Person(c, first)
    invite_member[p] = first
    invite_member[c] = second

    for i in range(1, length):
        p, c = invitation_pair[i]
        if c in invite_member.keys():
            continue
        else:
            p_ = invite_member[p]
            child = Person(c, p_)
            invite_member[c] = child

    score_rank = sorted(invite_member.items(), key=lambda item: item[1].score, reverse=True)
    answer = [score_rank[0][0], score_rank[1][0], score_rank[2][0]]
    return answer


print(solution([
    [1, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [5, 6],
    [5, 7],
    [6, 8],
    [2, 9]
]))
