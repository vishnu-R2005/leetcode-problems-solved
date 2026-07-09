class Solution:
    def primePalindrome(self, n: int) -> int:

        if 8 <= n <= 11:
            return 11

        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2

            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True

        x = 1
        while True:
            s = str(x)
            # Generate odd-length palindrome
            p = int(s + s[-2::-1])

            if p >= n and isPrime(p):
                return p

            x += 1