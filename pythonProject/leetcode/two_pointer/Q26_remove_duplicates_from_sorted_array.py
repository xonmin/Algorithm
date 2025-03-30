from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # by two pointer
        left, right = len(nums) - 2, len(nums) - 1
        count = 1

        while left >= 0:
            if nums[left] != nums[right]:
                count += 1
            else:
                nums.pop(right)

            right = left
            left -= 1
        return count


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
