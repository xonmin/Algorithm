def braces(values):
    ans = []
    dic = {'}': '{', ']': '[', ')': '('}
    open_bracket = ['{', '[', '(']

    for brackets in values:
        tmp = []
        for v in brackets:
            if v in open_bracket:
                tmp.append(v)
            else:
                if not tmp or tmp.pop() != dic[v]:
                    ans.append("NO")
                    break
        else:
            if len(tmp) == 0:
                ans.append("YES")
            else:
                ans.append("NO")

    return ans


print(braces(['{}[]()', '{[}]}', '{{']))
