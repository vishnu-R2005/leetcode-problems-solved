from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        comp = 0

        # Assign component IDs
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            component[i] = comp

        # Answer queries
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])

        return ans