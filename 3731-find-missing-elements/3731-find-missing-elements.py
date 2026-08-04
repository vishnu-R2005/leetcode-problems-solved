from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        ans = []

        for num in range(min(nums), max(nums) + 1):
            if num not in present:
                ans.append(num)

        return ans