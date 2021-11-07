from collections import deque


def solution(rows, columns):
    grid = [[0] * columns for _ in range(rows)]
    visited = [[0] * columns for _ in range(rows)]

    grid[0][0] = 1
    write_num = 1
    row, col = 0, 0

    q = deque()
    q.append([row, col, write_num])
    while q:
        for _ in grid:
            if 0 in _ :

        if 0 not in grid:
            break

        now_row, now_col, number = q.popleft()
        print(now_row,now_col,number)
        if number % 2 == 0:
            temp_row = now_row + 1
            temp_col = now_col
            print(temp_row,temp_col)
            if 0 <= temp_row < rows-1:
                grid[temp_row][temp_col] = number + 1
                q.append([temp_row, temp_col, number + 1])
            elif temp_row == rows-1:
                temp_row = 0
                grid[temp_row][temp_col] = number + 1
                q.append([temp_row, temp_col, number + 1])
        else:
            temp_row = now_row
            temp_col = now_col + 1

            if 0 <= temp_col < columns-1:
                grid[temp_row][temp_col] = number + 1
                q.append([temp_row, temp_col, number + 1])
            elif temp_col == columns-1:

                temp_col = 0
                grid[temp_row][temp_col] = number + 1
                q.append([temp_row, temp_col, number + 1])

    return grid

print(solution(3,4))