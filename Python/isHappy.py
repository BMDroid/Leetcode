class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        sums = []
        while s != '1':
            sum = 0
            for digit in s:
                sum += int(digit) ** 2
            if sum in sums:
                return False
            sums.append(sum)
            s = str(sum)
        print(sums)
        return True

    def isHappy2(self, n):
        sums = []
        while 1 not in sums:
            sum = 0
            while n != 0:
                n, r = divmod(n, 10)
                sum += r ** 2
            if sum in sums:
                return False
            n = sum
            sums.append(sum)
        print(sums)
        return True


if __name__ == '__main__':
    n = 19
    s = Solution()
    print(s.isHappy2(n))
