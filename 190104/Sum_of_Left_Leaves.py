# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, q = 0, root and [root]
        while q:
            top = q.pop()
            if top.left:
                ret += top.left.val if not top.left.right and not top.left.left else 0
                q.append(top.left)
            if top.right:
                q.append(top.right)
        return ret
