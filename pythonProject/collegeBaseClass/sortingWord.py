import sys
# Q1181 번

def solution(n):
    word_list = []
    for i in range(n):
        word_list.append(sys.stdin.readline().strip())

    word_list = list(set(word_list))
    word_list.sort(key=lambda x1: (len(x1), x1))

    for i in word_list:
        print(i)


n = int(sys.stdin.readline())

solution(n)
