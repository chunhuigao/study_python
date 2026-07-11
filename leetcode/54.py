class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        while True:
            print(left, right, top, bottom)
            # 从左到右
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # 从上到下
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # 从右到左
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            # 从下到上
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        
        return res