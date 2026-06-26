from typing import List
from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        class Fenwick:
            def __init__(self, n):
                self.bit = [0] * (n + 1)

            def update(self, i, val):
                while i < len(self.bit):
                    self.bit[i] += val
                    i += i & -i

            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        prefix = [0]
        cur = 0

        # +1 for target, -1 for others
        for x in nums:
            cur += 1 if x == target else -1
            prefix.append(cur)

        # Coordinate compression
        values = sorted(set(prefix))
        bit = Fenwick(len(values))

        ans = 0

        for x in prefix:
            idx = bisect_left(values, x) + 1
            ans += bit.query(idx - 1)   # count previous prefix sums < current
            bit.update(idx, 1)

        return ans