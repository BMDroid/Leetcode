def maxArea(height):
	left = 0
	right = len(height) - 1
	max = (right - left) * min(height[left], height[right])
	while left < right:
		if height[left] <= height[right]:
			left += 1
		else:
			right -= 1
		area = (right - left) * min(height[left], height[right])
		if area > max:
			max = area
	return max
	
if __name__ == '__main__':
	height = [1,8,6,2,5,4,8,3,7]
	max = maxArea(height)
	print(max)			
