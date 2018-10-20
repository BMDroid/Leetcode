class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        table = str.maketrans(dict.fromkeys(string.punctuation + ' '))
        s = s.translate(table).lower()
        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))