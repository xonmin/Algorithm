def solution(stockPrices, k):

    if len(stockPrices) < k:
        return 0
    dp = [1] * len(stockPrices)

    for i in range(len(stockPrices)):
        for j in range(len(stockPrices)):
            if stockPrices[i] > stockPrices[j]:
                dp[i] = max(dp[i],dp[j] +1)

    print(dp)
    return dp.count(k)


print(solution([1,2,3,3,4,5],3))