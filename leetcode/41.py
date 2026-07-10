class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            # 跳过负数
            if num <= 0:
                continue
            hashMap[num] = 1
        res = 100000000000
        # 1在哈希表
        if 1 in hashMap:
            for i in range(0,len(nums)):
                nn = nums[i]
                # 跳过负数
                if nn <= 0:
                    continue
                after = nn-1
                next = nn+1
                if after > 0 and after not in hashMap:
                    res = min(res,after)
                if next not in hashMap:
                    res = min(res,next)
        else:
            res = 1
        return res
       
    

result = Solution().firstMissingPositive([1])
print(result)