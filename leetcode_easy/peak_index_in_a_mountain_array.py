class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # option A
        
        # maxVal = max(arr)
        # return arr.index(maxVal)
        
        # option B
        
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start + end) / 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                start = mid
            elif arr[mid] > arr[mid + 1]:
                end = mid
        return mid