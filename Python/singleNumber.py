class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            i = nums.index(n)
            try:
                nums[i + 1::].index(n)
            except:
                return n

    def singleNumber2(self, nums):
        import operator
        from collections import Counter
        d = dict(Counter(nums))
        sortedDict = sorted(
            d.items(), key=operator.itemgetter(1), reverse=False)
        return sortedDict[0][0]


if __name__ == '__main__':
    nums = [2, 4, 1, 3, 2, 1, 3]
    s = Solution()
    print(s.singleNumber2(nums))
