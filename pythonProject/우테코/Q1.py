import sys

def solution(arr):
    answer = [0,0,0]

    num_count = [arr.count(1),arr.count(2),arr.count(3)]

    max_num = max(num_count)

    for i in range(3):

        add_number = max_num - num_count[i]
        for _ in range(add_number):
            answer[i] += 1

    return answer


