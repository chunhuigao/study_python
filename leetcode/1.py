class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i,num in enumerate(nums):
            hashMap[num] = i
        
        for i , num in enumerate(nums):
            j = hashMap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
        