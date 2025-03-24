from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = days
        meetings.sort(key=lambda x: x[0])

        merge_meetings = []

        for s, e in meetings:
            if not merge_meetings or merge_meetings[-1][1] < s - 1:
                merge_meetings.append([s, e])
            else:
                merge_meetings[-1][1] = max(merge_meetings[-1][1], e)

        available = sum(e - s + 1 for s, e in merge_meetings)
        return count - available


if __name__ == '__main__':
    # 10, [[5,7],[1,3],[9,10]]
    print(Solution().countDays(10, [[5, 7], [1, 3], [9, 10]]))
