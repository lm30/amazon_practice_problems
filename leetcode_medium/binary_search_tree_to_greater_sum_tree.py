# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root, 0)
        return root
    
    def dfs(self, node, currentSum):
        if node.right:
            node.val += self.dfs(node.right, currentSum)
        else:
            node.val += currentSum
        if node.left:
            leftVal = self.dfs(node.left, node.val)
            return leftVal
        return node.val