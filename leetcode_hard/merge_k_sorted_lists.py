from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        
        result = []
        for lst in lists:
            node = lst
            while node:
                heappush(result, (node.val, ListNode(node.val)))
                node = node.next
        
        if not result:
            return None
        
        node = heappop(result)[1]
        head = node
        nodeNext = None
        while result:
            nodeNext = heappop(result)[1]
            node.next = nodeNext
            node = nodeNext
        return head