class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(m):
            if m == 1:
                return False
            if 1 < m <= 3:
                return True
            if m % 2 == 0 or m % 3 == 0:
                return False
            i = 5
            while i ** 2 <= m:
                if m % i == 0 or m % (i + 2) == 0:
                    return False
                i += 6
            return True
        count = 0
        for num in range(1, n):
            if isPrime(num):
                count += 1
        return count

    def countPrimes2(self, n):
        notPrime = [False] * n
        count = 0
        for i in range(2, n):
            if not notPrime[i]:
                count += 1
                j = 2
                while i * j < n:
                    notPrime[i * j] = True
                    j += 1
        return count


if __name__ == '__main__':
    n = 10
    s = Solution()
    print(s.countPrimes2(n))
