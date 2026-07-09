class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums)+1)
      
        # 前缀和数组
        for i ,si in enumerate(nums):
            s[i+1] = s[i] + si
        res = 0

        # 哈希表
        d = dict()
        for i in range(len(s)):
            # 前缀和为k的子数组
            idx = s[i] - k
            # 在哈希表中能找到吗？
            if idx in d:
                res += d[idx]
            d[s[i]] = d.get(s[i],0) + 1
        return res

res = Solution().subarraySum([1],0)
print(res)