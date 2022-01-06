def solution(numbers, target):
    # brute Force 완전 탐색
    # 이 때 본인을 2번 호출하기 때문에 O(2^N)
    global count

    count = 0

    def dfs(idx, value, numbers, target):
        global count
        length = len(numbers)
        if idx == length:
            if value == target:
                count += 1
            return

        dfs(idx + 1, value + numbers[idx], numbers, target)
        dfs(idx + 1, value - numbers[idx], numbers, target)

    dfs(0, 0, numbers, target)

    return count


print(solution([1, 1, 1, 1, 1], 3))
