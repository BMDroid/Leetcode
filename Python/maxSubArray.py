def maxSubArray(nums):
    """
    : type nums: List[int]
    : rtype: int
    """
    left = 0
    right = len(nums) - 1
    max = sum(nums[left:right + 1])
    while left < right:
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
        else:
            if nums[left + 1] >= nums[right - 1]:
                right -= 1
            else:
                left += 1
        subSum = sum(nums[left:right + 1])
        if subSum > max:
            max = subSum
        print(left, right, max)
    return max


def maxSubArray1(nums):
    """
    : type nums: List[int]
    : rtype: int
    """
    left = 0
    right = len(nums) - 1
    max = sum(nums[left:right + 1])
    while left < right:
        sumLeft = nums[left] + nums[left + 1]
        sumRight = nums[right] + nums[right - 1]
        if sumLeft > sumRight:
            right -= 1
        elif sumLeft < sumRight:
            left += 1
        else:
            if nums[left] <= nums[right]:
                left += 1
            elif nums[left] > nums[right]:
                right -= 1
        subSum = sum(nums[left:right + 1])
        if subSum > max:
            max = subSum
        print(left, right, max)
    return max


def maxSubArray2(nums):
    """
    : type nums: List[int]
    : rtype: int
    """
    left = 0
    right = len(nums) - 1
    max = sum(nums[left:right + 1])
    subSum = 0
    for i in range(len(nums)):
        subSum += nums[i]
        if subSum > max:
            max = subSum
        if subSum < 0:
            subSum = 0
    return max


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
    nums = [0, 0, -3, 1]
    print(maxSubArray2(nums))
