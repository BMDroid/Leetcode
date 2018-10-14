def addBinary(a, b):
    """
    : type a: str
    : type b: str
    : rtype: str
    """
    l1 = [0] * max(len(a), len(b))
    l2 = [0] * max(len(a), len(b))
    l3 = [0] * (max(len(a), len(b)) + 1)
    for i, c in enumerate(a[::-1]):
        l1[-i - 1] = int(c)
    for j, d in enumerate(b[::-1]):
        l2[-j - 1] = int(d)
    for k, e in enumerate(l1[::-1]):
        if e + l2[-k - 1] + l3[-k - 1] >= 2:
            l3[-k - 1] = e + l2[-k - 1] + l3[-k - 1] - 2
            l3[-k - 1 - 1] += 1
        else:
            l3[-k - 1] += e + l2[-k - 1]
    if l3[0] == 0:
        return ''.join([str(c) for c in l3[1::]])
    return ''.join([str(c) for c in l3])


if __name__ == '__main__':
    #a = '11'
    #b = '1'
    a = "1010"
    b = "1011"
    #a = "1111"
    #b = "1111"
    print(addBinary(a, b))
