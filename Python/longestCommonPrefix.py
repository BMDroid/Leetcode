def longestCommonPrefix(strs):
   """
   :type strs: List[str]
   :rtype: str
   """
   prefix = ""
   if not strs:
       return prefix
   for i in range(len(strs[0])):
       temp = (strs[0])[i]
       for s in strs:
           if len(s) <= i or s[i] != temp:
               return prefix
       prefix += temp
   return prefix