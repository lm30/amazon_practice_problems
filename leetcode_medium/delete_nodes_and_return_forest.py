# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        output = []
        setToDelete = set(to_delete)
        self.dfs(root, output, None, setToDelete)
        return output
    
    def dfs(self, node, output, parent, todelete):
        if not node: 
            return
        
        if parent == None and node.val not in todelete:
            output.append(node)
        
        if node.val in todelete:
            todelete.remove(node.val)
            if node.left and node.left.val not in todelete: 
                output.append(node.left)
            if node.right and node.right.val not in todelete:
                output.append(node.right)
            
            if parent:
                if parent.left == node: parent.left = None
                if parent.right == node: parent.right = None
        
        self.dfs(node.left, output, node, todelete)
        self.dfs(node.right, output, node, todelete)