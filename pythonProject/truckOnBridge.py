from collections import deque


def solution(bridge_length, weight, truck_weights):
    second = 0
    wait_tr = deque(truck_weights)
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    w_on_bridge = 0

    while wait_tr:
        second += 1
        w_on_bridge -= bridge.popleft()
        if w_on_bridge + wait_tr[0] > weight:
            bridge.append(0)
        else:
            truck = wait_tr.popleft()
            w_on_bridge += truck
            bridge.append(truck)

    return second + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10]))
