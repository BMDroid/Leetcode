def zigzat_convert(s, n):
    if n == 1:
        return s
    a, b = divmod(len(s), 2 * n - 2)
    c, d = divmod(2 * n - 2, n)
    m = (c + d) * a + b
    t = [[]] * m
    for i in range(m):
        t[i] = [''] * n
    i, j = 0, 0
    for c in s:
        if i == 0 or i % (n - 1) == 0:
            t[i][j] = c
            j += 1
            if j == n:
                i += 1
                j = n - 1
                if j == 1:
                    j = 0
        else:
            j -= 1
            t[i][j] = c
            i += 1
            if j == 1:
                j = 0
        if i == m:
            break
    s = ''
    for i in range(n):
        s += ''.join([t[j][i] for j in range(m)])
    return t, s


def zigzat_convert1(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    pass


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    n = 9
    t, s = zigzat_convert(s, n)
    for l in t:
        print(l)
    print(s)
