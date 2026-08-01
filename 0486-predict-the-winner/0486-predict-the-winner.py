from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dfs(left, right):
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            pick_left = nums[left] - dfs(left + 1, right)
            pick_right = nums[right] - dfs(left, right - 1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return dfs(0, n - 1) >= 0