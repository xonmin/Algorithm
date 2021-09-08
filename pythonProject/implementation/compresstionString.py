
#

def solution(s):
    answer = 0

    for i in range(len(s)):
        temp_ans = 999999
        temp_ans = min(temp_ans,check(i,s))


    return answer

def check(token_len,s):
