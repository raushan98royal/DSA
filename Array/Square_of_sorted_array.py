#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, A):
        l=len(A)
        ans=[]
        for i in range(l):
            ans.append(A[i]**2)
        ans.sort()
        return ans