# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfsGrandchildren(root, None, None)
    
    def dfsGrandchildren(self, node, parent, grandparent):
        totalSum = 0
        if node.left:
            totalSum += self.dfsGrandchildren(node.left, node, parent)
        if node.right:
            totalSum += self.dfsGrandchildren(node.right, node, parent)
        
        if grandparent and grandparent.val % 2 == 0:
            totalSum += node.val
        return totalSum