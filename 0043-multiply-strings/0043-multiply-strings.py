class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                p1, p2 = i + j, i + j + 1

                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # Remove leading zeros
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        return "".join(map(str, res[i:]))