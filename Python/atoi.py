def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    valid = '0123456789+-'
    str = str.lstrip()
    # check empty string first if not will raise IndexError
    if len(str) == 0 or str[0] not in valid:
        return 0
    for i, c in enumerate(str[1:]):
        if c not in valid[0:10]:
            str = str[0:i + 1]
            break
    try:
        return int(s)
    except:
        return 0


if __name__ == '__main__':
    s = '--123+112'
    s = '42'
    print(myAtoi(s))
