# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        # traverse entire BST
        visited = set()
        count = [0]
        self.dfs(visited, root, L, R, count)
        return count[0]
        
    def dfs(self, visited, node, left, right, count):
        if not node:
            return
        if node not in visited:
            visited.add(node)
            if node.val >= left and node.val <= right:
                # if right between the left and right range, go to both sides
                count[0] += node.val
                self.dfs(visited, node.left, left, right, count)
                self.dfs(visited, node.right, left, right, count)
            elif node.val < left:
                self.dfs(visited, node.right, left, right, count)
            elif node.val > right:
                self.dfs(visited, node.left, left, right, count)