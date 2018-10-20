class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(sorted(nums)):
            if i != n:
                return i

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = set(range(len(nums) + 1))
        s2 = set(nums)
        return list(s1 - s2)[0]


if __name__ == '__main__':
    nums = [3, 0, 1]
    s = Solution()
    print(s.missingNumber(nums))
