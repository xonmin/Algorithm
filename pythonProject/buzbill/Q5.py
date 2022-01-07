def largestArea(samples):
    ans = 0
    size = len(samples[0])

    for i in range(1, size):
        for j in range(1, size):
            if samples[i][j] == 1:
                samples[i][j] = 1 + min(samples[i - 1][j], samples[i][j - 1], samples[i - 1][j - 1])
                ans = max(ans, samples[i][j])

    return ans


print(largestArea([[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
