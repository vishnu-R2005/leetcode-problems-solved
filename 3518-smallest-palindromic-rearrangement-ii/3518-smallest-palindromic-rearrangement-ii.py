class Solution:
    LIM = 1000001

    # Compute nCr, capped at LIM
    def comb(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)

        ans = 1
        for i in range(1, r + 1):
            ans = ans * (n - r + i) // i
            if ans >= self.LIM:
                return self.LIM
        return ans

    # Count distinct permutations of multiset
    def countWays(self, cnt) -> int:
        total = sum(cnt)
        ways = 1
        rem = total

        for x in cnt:
            if x == 0:
                continue
            ways *= self.comb(rem, x)
            if ways >= self.LIM:
                return self.LIM
            rem -= x

        return ways

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""

        for i in range(26):
            half[i] = freq[i] // 2
            if freq[i] % 2:
                mid = chr(i + ord('a'))

        if self.countWays(half) < k:
            return ""

        left = []
        half_len = len(s) // 2

        for _ in range(half_len):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(c + ord('a')))
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]