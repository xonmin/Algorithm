import math
from typing import List
class Solution:
    # rank = [1, 2, 3, 4, 5] -> 소요시간 : rank[i] * n^2
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low_time, high_time = 1,  max(ranks) * cars * cars

        while low_time < high_time:
            mid_time = (low_time + high_time) // 2
            repaired = 0

            # 각각의 rank (정비자) 에 대해 걸리는 시간 : T = rank[i] * n^2
            # mid_time >= rank[i] * n^2
            # n <= sqrt(mid_time / rank[i])
            for rank in ranks:
                count = int(math.sqrt(mid_time / rank))
                repaired += count

            if repaired < cars:
                low_time = mid_time + 1
            else:
                high_time = mid_time

        return low_time


if __name__ == '__main__':
    print(Solution().repairCars([4, 2, 3, 1], 10))
