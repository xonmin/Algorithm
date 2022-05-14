table, redo, answer = {}, [], []
select_row = -1


def select_upper_row(x):
    global select_row
    for i in range(x):
        select_row = table[select_row][0]


def select_lower_row(x):
    global select_row
    for i in range(x):
        select_row = table[select_row][1]


def delete_and_select_underRow():
    global select_row, table, redo, answer
    answer[select_row] = 'X'
    prev_e, next_e = table[select_row]
    redo.append([prev_e, select_row, next_e])

    if next_e == -1:
        select_row = table[select_row][0]
    else:
        select_row = table[select_row][1]

    if prev_e == -1:
        table[next_e][0] = -1
    elif next_e == -1:
        table[prev_e][1] = -1
    else:
        table[prev_e][1] = next_e
        table[next_e][0] = prev_e


def revive():
    global redo
    prev_e, now_e, next_e = redo.pop()
    answer[now_e] = 'O'
    if prev_e == -1:
        table[next_e][0] = now_e
    elif next_e == -1:
        table[prev_e][1] = now_e
    else:
        table[next_e][0], table[prev_e][1] = now_e, now_e


def solution(n, k, cmd):
    global table, select_row, answer
    answer = ['O'] * n
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0], table[n - 1], select_row = [-1,1], [n - 2, -1], k

    for i in cmd:
        if i == "C":
            delete_and_select_underRow()
        elif i == "Z":
            revive()
        else:
            c1, c2 = i.split()
            c2 = int(c2)
            if c1 == 'D':
                select_lower_row(c2)
            else:
                select_upper_row(c2)

    return ''.join(answer)


solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
