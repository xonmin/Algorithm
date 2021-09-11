
#문자열 압축 - 경우의 수
# 1~ len(S)까지에서 문자열 최소가 되는 경우를 찾기

def solution(s):
    answer = 0
    temp_ans = 999999
    for i in range(1,len(s)):

        temp_ans = min(temp_ans,check(i,s))
       # print(temp_ans)

    #print(temp_ans)
    return answer

def check(token_len,s):
    compressed_list = list()
    tokenization_list = [s[i:i+token_len] for i in range(0,len(s),token_len)]

    compressed_list.append([1,tokenization_list[0]])
    length = len(tokenization_list)

    for i in range(1,length):
        compare_beforeValue =  compressed_list.pop()
        compressed_list.append(compare_beforeValue)
        #이전 값이랑 문자가 같으면
        if tokenization_list[i] == compare_beforeValue[1]:
            #기존 꺼 제거 , 값 증가
           compressed_list.pop()
           compare_beforeValue[0] +=1
           compressed_list.append(compare_beforeValue)
          # print(compressed_list)
        else:
            compressed_list.append([1,tokenization_list[i]])
           # print(compressed_list)

    my_list = sum(compressed_list, [])

    pressed_string = "".join(map(str,my_list))
    # 1제거
    pressed_string = pressed_string.replace("1","")
    #print(pressed_string)
    return len(pressed_string)








solution("abcabcdede")