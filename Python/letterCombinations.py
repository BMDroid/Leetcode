def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
        return []
    import random
    dic = {'2': 'a b c', '3': 'd e f', '4': 'g h i', '5': 'j k l',
           '6': 'm n o', '7': 'p q r s', '8': 't u v', '9': 'w x y z'}
    st = []
    n = 1
    for d in digits:
        st.append(dic[d])
        n *= len(dic[d].replace(' ', ''))
    comb = []
    while len(comb) < n:
        c = ''.join([random.choice(s.split()) for s in st])
        if c not in comb:
            comb.append(c)
    return comb


if __name__ == '__main__':
    comb = letterCombinations('345678')
    print(comb)
