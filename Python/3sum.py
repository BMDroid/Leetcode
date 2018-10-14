def three_sum(nums):
    if len(nums) < 3:
        return []
    hist = {nums[0]: 0}
    lst = []
    t = []
    for i in range(len(nums)):
        target = -1 * nums[i]
        for j in range(len(nums)):
            if hist.get(target - nums[j], -1) != -1:
                if set((nums[i], nums[j], nums[hist[target - nums[j]]])) not in t:
                    if i != j and j != hist[target - nums[j]] and i != hist[target - nums[j]]:
                        lst.append(
                            [nums[i], nums[j], nums[hist[target - nums[j]]]])
                        t.append(
                            set((nums[i], nums[j], nums[hist[target - nums[j]]])))
                        # hist[nums[j]] = j
                        break
            else:
                hist[nums[j]] = j
    print(hist)
    return lst


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, 3, -7, 4]

    nums = [-2, 0, 1, 1, 2]
    nums = [-2, 0, 0, 2, 2]
    nums = [3, 0, -2, -1, 1, 2]
    nums = [13, 14, 1, 2, -11, -11, -1, 5, -1, -11, -9, -12, 5, -3, -7, -4, -12, -9, 8, -13, -8, 2, -6, 8, 11, 7, 7, -6, 8, -9, 0, 6, 13, -14, -15, 9, 12, -9, -9, -4, -4, -3, -9, -14, 9, -8, -11, 13, -10, 13, -15, -11, 0, -14, 5, -
            4, 0, -3, -3, -7, -4, 12, 14, -14, 5, 7, 10, -5, 13, -14, -2, -6, -9, 5, -12, 7, 4, -8, 5, 1, -10, -3, 5, 6, -9, -5, 9, 6, 0, 14, -15, 11, 11, 6, 4, -6, -10, -1, 4, -11, -8, -13, -10, -2, -1, -7, -9, 10, -7, 3, -4, -2, 8, -13]
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 3, 0, 1, 1, -1, -5, -5, 3, -3, -3, 0]
    nums = [0, 0, 0, 0, 1]
    t = three_sum(nums)
    print(t)
