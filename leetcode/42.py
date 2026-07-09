class Solution:
    def trap(self, height: List[int]) -> int:
        ll = len(height)
        if ll < 3:
            return 0
        left = []
        temp = height[0]
        for i in range(ll):
            left.append(max(temp, height[i]))
            temp = max(temp, height[i])
        right = [-1]*ll
        temp = height[-1]
        for i in range(ll-1, -1, -1):
            right[i] = (max(temp, height[i]))
            temp = max(temp, height[i])
        area = 0
        for i in range(ll):
            area += min(left[i], right[i]) - height[i]
        return area
result = Solution().trap([4,2,0,3,2,5])
print(result)
