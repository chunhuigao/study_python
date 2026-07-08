class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = [height[0]]
        for i in range(1,len(height)):
            left.append(max(left[i-1], height[i]))
        right = [-1] * len(height)
        right[len(height)-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        l = 0
        r = len(height)-1
        area = 0
        while l < r:
            area = max(area, min(left[l], right[r]) * (r - l))
            if left[l] < right[r]:
                l += 1
            else:
                r -= 1
        return area
res = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(res)  