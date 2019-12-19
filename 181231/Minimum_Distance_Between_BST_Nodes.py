# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        v = []
        def travel(tree):
            if not tree:
                return
            v.append(tree.val)
            travel(tree.left)
            travel(tree.right)
        travel(root)
        res = 1000000
        v.sort()
        for i in range(1, len(v)):
            if v[i] - v[i-1] < res:
                res = v[i] - v[i-1]
            if res == 1:
                break
        return res