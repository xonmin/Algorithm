# 1157번 단어 공부

import sys
import string

input_string = sys.stdin.readline().rstrip()
upper = input_string.upper()
set_input_str = set(upper)

word_list = {i: 0 for i in upper}

for c in upper:
    word_list[c] += 1

ans = [k for k, v in word_list.items() if max(word_list.values()) == v]
if len(ans) > 1:
    print('?')
else:
    print(ans[0])


