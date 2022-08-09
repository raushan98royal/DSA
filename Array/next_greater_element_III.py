#Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

class Solution:
  def nextGreaterElement(self, n: int) -> int:
    def nextPermutation(s: List[chr]) -> str:
      i = len(s) - 2
      while i >= 0:
        if s[i] < s[i + 1]:
          break
        i -= 1

      if i >= 0:
        for j in range(len(s) - 1, i, -1):
          if s[j] > s[i]:
            break
        s[i], s[j] = s[j], s[i]

      reverse(s, i + 1, len(s) - 1)
      return ''.join(s)

    def reverse(s: List[chr], l: int, r: int):
      while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    s = nextPermutation(list(str(n)))
    ans = int(s)
    return -1 if ans > 2**31 - 1 or ans <= n else ans