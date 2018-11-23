# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if self.getLeaf(root1) == self.getLeaf(root2):
            return self.getLeaf(root2)
        else:
            return False

    def getLeaf(self, root):
        ret, stack = [], []
        if not root:
            return []
        while root:
            q.append(root)
            root = root.left

        ret.append(root)
        while stack:
            top = stack.pop()
            
