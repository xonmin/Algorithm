def solution(s):
    answer = []

    chk_count = 1
    origin_len = len(s)
    s = s + s
    s_len = len(s)

    for i in range(s_len):

        if i > origin_len - 1:
            if s[i] == s[i + 1]:
                chk_count += 1
            else:
                answer.pop(0)
                answer.append(chk_count)
                break
        else:
            if s[i] == s[i + 1]:
                chk_count += 1
            else:
                answer.append(chk_count)
                chk_count = 1

    answer.sort()
    return answer
