class Solution:
    '''
    :type n: int
    :rtype int
    '''

    def reverseBits(self, n):
        s = []
        while n != 0:
            n, r = divmod(n, 2)
            s.append(r)
        for i in range(32 - len(s)):
            s.append(0)
        num = 0
        for i, b in enumerate(s[::-1]):
            num += b * 2 ** i
        return num

    def reverseBits2(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    n = 43261596
    print(s.reverseBits(n))
    n = '00000010100101000001111010011100'
