from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        order = sorted((nums[i], i) for i in range(n))

        values = [x for x, _ in order]

        pos = [0] * n
        for i, (_, idx) in enumerate(order):
            pos[idx] = i

        # Component IDs
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # next[i] = farthest reachable index in one edge
        nxt = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1
            nxt[i] = r

        LOG = n.bit_length()

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a > b:
                a, b = b, a

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt_pos = up[k][cur]
                if nxt_pos < b:
                    cur = nxt_pos
                    steps += 1 << k

            ans.append(steps + 1)

        return ans