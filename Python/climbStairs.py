def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    import math
    count = 0
    a, _ = divmod(n, 2)
    for a in range(a + 1):
        count += math.factorial(n - a) / \
            (math.factorial(a) * math.factorial(n - 2 * a))
    return int(count)


if __name__ == '__main__':
    n = 1
    print(climbStairs(n))
