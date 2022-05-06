answer = 0


def insert_item(bucket, item):
    global answer
    if len(bucket) == 0:
        bucket.append(item)
        return
    last = bucket[-1]
    if item == last:
        bucket.pop()
        answer += 2
    else:
        bucket.append(item)


def solution(board, moves):
    bucket = []
    global answer

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            else:
                item = board[i][m-1]
                board[i][m-1] = 0
                insert_item(bucket, item)
                break

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
