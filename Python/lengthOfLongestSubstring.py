def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == len(set(s)):
        return len(s)
    step = len(set(s))
    longestLength = 0
    while step > 0:
        for i in range(len(s) - step + 1):
            sub = s[i:i + step]
            if len(sub) == len(set(sub)) and len(sub) > longestLength:
                longestLength = len(sub)
                if longestLength == step:
                    return longestLength
        step -= 1
    return longestLength


if __name__ == '__main__':
    # s = 'abcabcbb'
    s = 'aab'
    print(lengthOfLongestSubstring(s))
