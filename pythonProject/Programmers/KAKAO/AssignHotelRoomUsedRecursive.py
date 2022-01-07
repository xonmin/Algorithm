from collections import defaultdict
import sys

sys.setrecursionlimit(2500)

def findEmpty(number, rooms):  # 빈 방 찾기
    if number not in rooms:
        rooms[number] = number + 1
        return number

    empty = findEmpty(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    req = len(room_number)

    counter = defaultdict(int)
    ans = []

    for i in range(req):
        candidate_room = findEmpty(room_number[i], counter)
        ans.append(candidate_room)

    return ans


print(solution(10, [1, 3, 4, 1, 3, 1]))
