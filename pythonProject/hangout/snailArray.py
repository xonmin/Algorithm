def solution(n):
    snail = [[0] * n for i in range(n)]

    row = -1
    col = 0
    num = 0
    # 한 줄의 간격
    size = n
    #O(n^2)
    while num <= n * n:
        print(size)
        for _ in range(size):  # 좌 - 우
            num += 1
            row += 1
            snail[col][row] = num

        size -= 1

        if size == 0:
            break

        for _ in range(size):  # 상 - 하
            num += 1
            col += 1
            snail[col][row] = num

        for _ in range(size):  # 우 - 좌
            num += 1
            row -= 1
            snail[col][row] = num

        size -= 1

        if size == 0:
            break

        for _ in range(size):  # 하 - 상
            num += 1
            col -= 1
            snail[col][row] = num

    for i in snail:
        print(i)


solution(6)
