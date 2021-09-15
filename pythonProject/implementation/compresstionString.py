import re


def solution(s):
    answer = 0
    temp_ans = 999999

    # 문자열 길이가 1일 때
    if (len(s) == 1):
        answer = 1
        #print(answer)
        return answer

    for i in range(1, len(s)):
        compressed_list = list()
        tokenization_list = [s[j:j + i] for j in range(0, len(s), i)]

        compressed_list.append([1, tokenization_list[0]])
        length = len(tokenization_list)

        for i in range(1, length):
            compare_beforeValue = compressed_list.pop()
            compressed_list.append(compare_beforeValue)
            # 이전 값이랑 문자가 같으면
            if tokenization_list[i] == compare_beforeValue[1]:
                # 기존 꺼 제거 , 값 증가
                compressed_list.pop()
                compare_beforeValue[0] += 1
                compressed_list.append(compare_beforeValue)
            # print(compressed_list)
            else:
                compressed_list.append([1, tokenization_list[i]])


        my_list = sum(compressed_list, [])

        pressed_string = "".join(map(str, my_list))
        # 1제거

        try:
            for j in range(0, len(pressed_string) - 1):
                #print(re.findall("[a-zA-Z]", pressed_string[j + 1]))
                if pressed_string[j] == "1" and re.findall("[a-zA-Z]", pressed_string[j + 1]) != []:
                    pressed_string = pressed_string[:j] + pressed_string[j+1:]
                    #print(j,'번째',"1제거하러", pressed_string)
            #print(pressed_string)

        except:
            pass

    temp_ans = min(temp_ans, len(pressed_string))
    print(temp_ans)
    answer = temp_ans
    return answer


solution("aaaaaaaaaabb")
