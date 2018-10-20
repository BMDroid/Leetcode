class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        dic = dict(zip(string.ascii_uppercase, range(1, 27)))
        num = 0
        for i, letter in enumerate(s):
            num += dic[letter] * 26**(len(s) - i - 1)
        return num


if __name__ == '__main__':
    solution = Solution()
    s = 'AC'
    print(solution.titleToNumber(s))
