# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        self.traverseBST(root, val)
        return root
    
    def traverseBST(self, node, val):
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.traverseBST(node.right, val)
        elif val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.traverseBST(node.left, val)