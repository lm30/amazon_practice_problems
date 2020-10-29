class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap) == 0 or self.maxHeap[0] <= num:
            heappush(self.maxHeap, num)
        else:
            heappush(self.minHeap, -num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return float(self.maxHeap[0] + -self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        else:
            return self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()