from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        hasOdd = False

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                hasOdd = True

        return length + 1 if hasOdd else length