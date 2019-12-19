# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res, q, v = -1, root and [root], []
        while q:
            top = q.pop()
            v.append(top.val)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        v.sort()
        for i in range(1, len(v)):
            temp = v[i] - v[i-1]
            if res == -1 or temp < res:
                res = temp
            if res == 0:  # res is not smaller than zero
                return res
        return res