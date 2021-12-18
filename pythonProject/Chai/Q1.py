from collections import deque


def reductionCost(num):
    tmp = []
    num_list = num

    while True:
        length = len(num_list)
        if length == 1:
            break

        num_list.sort()
        num1, num2 = num_list[0], num_list[1]
        num_list.remove(num1)
        num_list.remove(num2)
        num_list.append(num1 + num2)
        tmp.append(num1 + num2)

    ans = sum(tmp)
    return ans


print(reductionCost([1, 2, 3]))
