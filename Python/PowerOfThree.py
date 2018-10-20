class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return Solution.isPowerOfThree(self, n / 3)


if __name__ == '__main__':
    s = Solution()
    n = 27
    print(s.isPowerOfThree(n))
