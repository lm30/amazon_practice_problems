# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        self.inorderTraversal(root, arr)
        node = self.constructTree(arr)
        return node
    
    def inorderTraversal(self, node, arr):
        if not node:
            return
        self.inorderTraversal(node.left, arr)
        arr.append(node.val)
        self.inorderTraversal(node.right, arr)
    
    def constructTree(self, arr):
        if len(arr) == 0:
            return None
        
        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        
        node.left = self.constructTree(arr[:mid])
        node.right = self.constructTree(arr[mid + 1:])
        
        return node