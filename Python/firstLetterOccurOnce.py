def first_letter_occur_once(s):
    for i, letter in enumerate(s):
        if s.count(letter) == 1:
            return i
    return - 1


def first_letter_occur_once1(s):
    d = {}
    for i, letter in enumerate(s):
        d[letter] = d.get(letter, []) + [i]
    for letter in s:
        if len(d[letter]) == 1:
            return d[letter][0]
    return -1


if __name__ == '__main__':

    s = 'abccdabe'
    s = 'aa'
    s = ''
    print(first_letter_occur_once(s))
