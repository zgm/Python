class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m*n-1
        while L<=R:
            mid = (L+R)/2
            if matrix[mid/n][mid%n]==target:
                return True
            if matrix[mid/n][mid%n]<target:
                L = mid+1
            else:
                R = mid-1
        return False

