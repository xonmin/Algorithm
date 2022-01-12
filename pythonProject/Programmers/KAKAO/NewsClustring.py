import re
import string


def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []

    str2 = str2.lower()
    str1 = str1.lower()

    for i in range(len(str1) - 1):
        set1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        set2.append(str2[i:i + 2])

    set1 = [word for word in set1 if word.isalpha()]
    set2 = [word for word in set2 if word.isalpha()]

    intersection = []
    set1_copy = set1.copy()

    for i in set1:
        if i in set2:
            intersection.append(i)
            set1_copy.remove(i)
            set2.remove(i)

    union = set1_copy + set2 + intersection
  
    if not set1 and not set2:
        return 65536

    return int((len(intersection) / len(union)) * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
print(solution("A+C","DEF"))
