# 90도 회전
def solution(arr):
    arr_len = len(arr)
    copy_arr = [[0] * arr_len for i in range(arr_len)]

    for i in range(arr_len):
        for j in range(arr_len):
            copy_arr[j][arr_len - 1 - i] = arr[i][j]

    return copy_arr


ans = solution([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

#180도 회전
real_ans = solution(ans)
for i in real_ans:
    print(i)
