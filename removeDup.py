import sys

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n<=0: return 0
        m, dup = 1, 1
        for i in range(1,n):
            if A[i-1]==A[i]:
                dup += 1
                if dup<=2:
                    A[m] = A[i]
                    m += 1
            else:
                dup = 1
                A[m] = A[i]
                m += 1
        return m


s = Solution()
print s.removeDuplicates([])
print s.removeDuplicates([1,1,1,2,2,3])
