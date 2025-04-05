import operator
from itertools import combinations
from typing import List
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset_len = len(nums)
        xor_sum = 0
        for i in range(1, subset_len + 1):

            for subset in combinations(nums, i):
                xor = reduce(operator.xor, subset)

                xor_sum += xor

        return xor_sum


if __name__ == "__main__":
    print(Solution().subsetXORSum([1, 3]))
