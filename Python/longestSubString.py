def longest_sub_str(s):
    if len(s) <= 1:
        return 1
    curMax = 0
    left = 0
    right = 0
    while right < len(s):
        i = left
        while i < right:
            if s[i] == s[right]:
                left = i + 1
                break
            i += 1
        curMax = max(curMax, right - left + 1)
        right += 1
    return curMax


s = 'abbca'
print(longest_sub_str(s))
