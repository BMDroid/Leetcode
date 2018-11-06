class Solution:
    def findUnsortedSubarray(self, nums):  # Exceed Time Limit
        """
        :type nums: List[int]
        :rtype: int
        """
        swapIndices = []
        swap = True
        while swap:
            swap = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapIndices.append(i)
                    swap = True
        return max(swapIndices) - min(swapIndices) + 2 if len(swapIndices) > 0 else 0

    def findUnsortedSubarray2(self, nums):  # wrong answer
        swapIndices = []
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapIndices.append(i)
        return max(swapIndices) - min(swapIndices) + 2 if len(swapIndices) > 0 else 0
