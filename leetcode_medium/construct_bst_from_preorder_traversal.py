# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        rootNode = TreeNode(preorder[0], None, None)
        
        for item in preorder:
            self.constructBST(rootNode, item)
        
        return rootNode
        
    def constructBST(self, node, item):
        if node.val > item:
            if node.left == None:
                node.left = TreeNode(item, None, None)
            else:
                self.constructBST(node.left, item)
        elif node.val < item:
            if node.right == None:
                node.right = TreeNode(item, None, None)
            else:
                self.constructBST(node.right, item)