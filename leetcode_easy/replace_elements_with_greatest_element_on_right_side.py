class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
#         for i in range(len(arr)):
#             if i >= len(arr) - 1:
#                 arr[i] = -1
#             else:
#                 arr[i] = max(arr[i + 1:])
#         return arr
        
        # much faster since not calling max all the time
        if len(arr) == 1:
            return [-1]
        
        maxVal = max(arr[1:])
        for i in range(len(arr) - 1):
            if arr[i] >= maxVal:
                maxVal = max(arr[i + 1:])
            arr[i] = maxVal
        
        arr[-1] = -1
        return arr