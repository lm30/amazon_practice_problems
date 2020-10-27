class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return []
        
        nums.sort()
        firstPtr = 0
        secondPtr = firstPtr + 1
        result = []
        
        while secondPtr < len(nums):
            if nums[firstPtr] == nums[secondPtr]:
                result.append(nums[firstPtr])
            firstPtr += 1
            secondPtr += 1
        
        return result