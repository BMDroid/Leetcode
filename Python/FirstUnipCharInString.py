class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        dic = dict(Counter(s))
        for i, letter in enumerate(s):
            if dic[letter] == 1:
                return i
        return - 1
