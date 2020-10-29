class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        heap = []
        count = collections.defaultdict(int)
        for idx in range(k):
            heappush(heap, -nums[idx])
        
        result.append(-heap[0])
        for i in range(1, len(nums) - k + 1):
            heappush(heap, -nums[i + k - 1])
            count[-nums[i-1]] += 1
            while count[heap[0]] > 0:
                count[heap[0]] -= 1
                heappop(heap)
            result.append(-heap[0])
        return result