from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Segment tree node: (count_non_zero, value, digit_sum)
        seg = [(0, 0, 0)] * (4 * n)

        def merge(left, right):
            c1, v1, s1 = left
            c2, v2, s2 = right
            return (
                c1 + c2,
                (v1 * pow10[c2] + v2) % MOD,
                s1 + s2
            )

        def build(idx, l, r):
            if l == r:
                d = int(s[l])
                if d == 0:
                    seg[idx] = (0, 0, 0)
                else:
                    seg[idx] = (1, d, d)
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])

        def query(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                return seg[idx]

            mid = (l + r) // 2

            if qr <= mid:
                return query(idx * 2, l, mid, ql, qr)

            if ql > mid:
                return query(idx * 2 + 1, mid + 1, r, ql, qr)

            left = query(idx * 2, l, mid, ql, qr)
            right = query(idx * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)

        build(1, 0, n - 1)

        ans = []
        for l, r in queries:
            _, value, digit_sum = query(1, 0, n - 1, l, r)
            ans.append((value * digit_sum) % MOD)

        return ans