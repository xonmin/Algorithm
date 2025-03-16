chart = [['-' for col in range(50)] for row in range(50)]
dict_locate = dict()
merge_locate = dict()


def update_merge_dict(r1, c1, r2, c2):
    global merge_locate
    for r in (r1-1, r2):
        for c in (c1-1, c2):
            merge_locate[[r,c]]

def update_dict(r, c, value):
    global dict_locate
    if value not in dict_locate.keys():
        dict_locate[value] = []
    dict_locate[value].append([r, c])


def update(r, c, value):
    global chart
    chart[r - 1][c - 1] = value
    update_dict(r - 1, c - 1, value)


def update(v1, v2):
    global chart, dict_locate
    locate = dict_locate.pop(v1)

    for r, c in locate:
        chart[r][c] = v2
    dict_locate[v2] = locate


def merge(r1, c1, r2, c2):
    global chart


def unmerge(r, c):
    global chart


def print(r, c):
    global chart


def solution(commands):
    for c in commands:
