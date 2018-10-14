def isValid(s):
  pList = []
  pDict = {'(': ')', '{': '}', '[' : ']'}
  for p in s:
      if p in list(pDict):
          pList.append(p)
      else:
          if len(pList) == 0:
              return False
          elif pDict.get(pList[-1]) != p:
              return False
          else:
              pList.pop()
  if len(pList) == 0:
      return True
  return False