class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_matrix = len(matrix)
        m = len_matrix//2
        n = (len_matrix +1 )//2
        for i in range(m):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len_matrix-j-1][i]
                matrix[len_matrix-j-1][i] = matrix[len_matrix-i-1][len_matrix-j-1]
                matrix[len_matrix-i-1][len_matrix-j-1] = matrix[j][len_matrix-i-1]
                matrix[j][len_matrix-i-1] = temp
        return matrix
    
result = Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
print(result)
