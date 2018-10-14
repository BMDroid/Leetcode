def strStr(haystack, needle):
    """Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    :type haystack: str
    : type needle: str
    : rtype: int
    """
    if needle not in haystack:
        return -1
    if needle == '':
        return 0
    d = {}
    for i, c in enumerate(haystack):
        d[c] = d.get(c, []) + [i]
    for v in d[needle[0]]:
        if haystack[v: v + len(needle)] == needle:
            return v
