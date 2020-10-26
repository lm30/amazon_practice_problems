"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# recursive solution
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.postOrder(root, result)
        return result
        
    def postOrder(self, node, result):
        for child in node.children:
            self.postOrder(child, result)
        result.append(node.val)