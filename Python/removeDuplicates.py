def removeDuplicates(nums):
   """
   :type nums: List[int]
   :rtype: int
   """
   if not nums:
       return 0
   temp = nums[0]
   i = 1
   while i < len(nums):
      if nums[i] == temp:
          nums.pop(i)
      else:
          temp = nums[i]
          i += 1
   return len(nums)

list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(list))
print(list)