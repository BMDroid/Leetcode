from collections import Counter


class Solution:

    def longestPalindrome(self, s):
        """
        : type s: str
        : rtype: int
        """
        c = Counter(s)
        odd = False
        length = 0
        for n in c.values():
            if n % 2 == 0:
                length += n
            else:
                odd = True
        length += n - 1
        if odd:
            return length + 1
        return length
