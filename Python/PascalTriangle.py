class Solution:
    def generate(self, numRows):
        """
        : type numRows: int
        : rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        tri = [[1]]
        for i in range(1, numRows):
            t = [1]
            for j in range(1, i):
                t.append(tri[i - 1][j - 1] + tri[i - 1][j])
            t.append(1)
            tri.append(t)
        return tri


if __name__ == '__main__':
    s = Solution()
    numRows = 10
    print(s.generate(numRows))
