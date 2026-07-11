class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = 0
        while m >= 0 and n <= len(matrix[0])-1:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False