# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        levelSums = {}
        self.dfs(root, 1, levelSums)
        maxVal = max(levelSums.values())
        for k in levelSums:
            if levelSums[k] == maxVal:
                return k
        
    def dfs(self, node, level, levelSums):
        if not node:
            return

        if level in levelSums:
            levelSums[level] += node.val
        else:
            levelSums[level] = node.val
        
        self.dfs(node.left, level + 1, levelSums)
        self.dfs(node.right, level + 1, levelSums)