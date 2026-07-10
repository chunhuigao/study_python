class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        x = set()
        y = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
        for i in range(m):
            for j in range(n):
                if i in x or j in y:
                    matrix[i][j] = 0
        return matrix