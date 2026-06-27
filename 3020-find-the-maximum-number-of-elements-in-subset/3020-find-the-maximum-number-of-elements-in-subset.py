from collections import Counter

class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        ans = 1

        # Special handling for 1
        if 1 in freq:
            c = freq[1]
            if c % 2 == 0:
                c -= 1
            ans = max(ans, c)

        for x in freq:
            if x == 1:
                continue

            length = 0
            curr = x

            while curr in freq:
                if freq[curr] >= 2:
                    length += 1
                    curr = curr * curr
                else:
                    length += 1
                    break

            # total elements = 2 * length - 1
            ans = max(ans, 2 * length - 1)

        return ans
        