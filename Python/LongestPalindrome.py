def longestPalindrome(s):
    import operator
    d = dict()
    for i, c in enumerate(s):
        d[c] = d.get(c, []) + [i]
    return d


print(longestPalindrome('babad'))
