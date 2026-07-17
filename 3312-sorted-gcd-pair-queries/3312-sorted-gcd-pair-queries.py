class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
       
        MAX = max(nums)

        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (MAX + 1)

        for d in range(1, MAX + 1):
            for m in range(d, MAX + 1, d):
                cnt[d] += freq[m]

        # exact[d] = pairs with gcd exactly d
        exact = [0] * (MAX + 1)

        for d in range(MAX, 0, -1):
            c = cnt[d]
            exact[d] = c * (c - 1) // 2
            for m in range(d * 2, MAX + 1, d):
                exact[d] -= exact[m]

        prefix = []
        values = []

        total = 0
        for g in range(1, MAX + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans