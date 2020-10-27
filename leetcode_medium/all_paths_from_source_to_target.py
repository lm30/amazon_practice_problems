class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        output = []
        trackingList = [0]
        self.backtrack(graph, target, output, trackingList, 0)
        return output

    def backtrack(self, graph, target, output, trackingList, nodeIndex):
        if nodeIndex == target:
            output.append(trackingList[:])
            return
        
        for i in graph[nodeIndex]:
            trackingList.append(i)
            self.backtrack(graph, target, output, trackingList, i)
            trackingList.pop()