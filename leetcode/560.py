class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums)+1)
      
        for i ,si in enumerate(nums):
            s[i+1] = s[i] + si
        res = 0

        d = dict()
        for i in range(len(s)):
            idx = s[i] - k
            if idx in d:
                res += d[idx]
            d[s[i]] = d.get(s[i],0) + 1
        return res

res = Solution().subarraySum([1],0)
print(res)