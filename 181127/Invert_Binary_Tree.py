# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def bfs(root):
            if not root:
                return None
            else:
                t = root.left
                root.left = root.right
                root.right = t
                bfs(root.left)
                bfs(root.right)
        bfs(root)
        return root
