class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i]
            if i != n-1-i:
                res += mat[i][n-1-i]
        return res