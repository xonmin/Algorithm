from collections import defaultdict

def solution(k, room_number):
    req = len(room_number)

    counter = defaultdict(int)

    for i in range(req):
        candidate_room = room_number[i]
        while True:
            if counter[candidate_room] == 0:
                break
            else:
                candidate_room += 1

        counter[candidate_room] = i + 1

    ans = list(counter.keys())
    return ans


print(solution(10, [1, 3, 4, 1, 3, 1]))
