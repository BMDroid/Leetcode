def isPalindrome(x):
  # numStr = str(x)
  numStr = f"{x}"
  for i in range(int(len(numStr) / 2)):
    if numStr[i] != numStr[len(numStr) - 1 - i]:
      return False
  return True