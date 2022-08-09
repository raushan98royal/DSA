#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than [n / 2] times.

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    ans = None
    count = 0

    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)

    return ans