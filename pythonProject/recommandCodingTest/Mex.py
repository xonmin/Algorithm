

def solution(arr, x):
    arr_length = len(arr)
    mod_arr = list()

    for i in arr:
        r, q = divmod(i, x)
        mod_arr.append(q)

    num_mod = list()

    for i in range(x):
        num_mod.append(mod_arr.count(i))

    min_num = min(num_mod)

    return x * min_num + num_mod.index(min_num)


print(solution([0, 1, 2, 2, 0, 0, 10, 3], 3))


def solution2(arr, x):
    arr_length = len(arr)
    mod_arr = list()

    for i in arr:
        r, q = divmod(i, x)
        mod_arr.append(q)

    num_mod = list()

    for i in range(x):
        num_mod.append([mod_arr.count(i), i])

    num_mod.sort(key=lambda x: x[0])

    min_num = num_mod[0][0]
    min_idx = num_mod[0][1]

    return x * min_num + min_idx


print(solution([0, 1, 2, 2, 0, 0, 10, 3], 3))


