# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    vp = []
    vq = []
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def travel(root, value_list):
            if not root:
                value_list.append(-1)
                return
            value_list.append(root.val)
            travel(root.left, value_list)
            travel(root.right, value_list)

        travel(p, self.vp)
        travel(q, self.vq)

        return self.vq == self.vp

# TODO:
# This question is actually solved but the leetcode didn't pass the code
# I get the right ans while using "run the code" but get the contary result while submit.
