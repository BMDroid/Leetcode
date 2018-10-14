def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        if len(s) == 0:
            return 0
        numList = []
        for r in s:
            numList.append(romanDict.get(r))
        num = 0
        for i in range(0, len(s)):
            if(i < len(s) - 1 and numList[i] < numList[i + 1]):
                numList[i] = -1 * numList[i]
            num += numList[i]
        return num