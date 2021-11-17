def solution(skill, skill_trees):
    answer = 0

    for sk_tr in skill_trees:
        st = list()
        for s in sk_tr:
            if s in skill:
                st.append(s)

        sk_tr = ''.join(st)
        #sk_tr = ''.join([st for st in sk_tr if st in skill])
        if skill.startswith(sk_tr):
            answer += 1
    return answer
