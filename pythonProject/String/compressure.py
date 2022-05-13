import itertools
import string

comp_dict, answer = {}, []


def find_correct_longest_string(sub_string):
    global comp_dict
    l, candidate = len(sub_string), ''
    for i in range(1, l+1):
        if sub_string[:i] in comp_dict:
            candidate = sub_string[:i]
    return candidate


def print_index_and_delete_sub_string(sub_string, origin_string):
    global comp_dict, answer
    answer.append(comp_dict[sub_string])
    return origin_string.replace(sub_string,"",1).strip()


def register_word(w, c):
    global comp_dict
    comp_dict[w + c] = len(comp_dict) + 1


def solution(msg):
    global comp_dict, answer
    num = 1
    for i in string.ascii_uppercase:
        comp_dict[i] = num
        num += 1  # 마지막은 27로 설정됨

    while len(msg) != 0:
        sub_string = find_correct_longest_string(msg)
        msg = print_index_and_delete_sub_string(sub_string, msg)
        if len(msg) != 0:
            register_word(sub_string, msg[0])
    return answer

