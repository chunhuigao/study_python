class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for num in s:
            ## 神来之笔
            if num - 1 in s:
                continue
      
            next = num + 1
            while next in s:
                next += 1
            l = max(l, next - num)
        return l