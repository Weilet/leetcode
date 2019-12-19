# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def func(pre_list, post_list):
            if len(pre_list) == 0:
                return None
            node = TreeNode(pre_list[0])
            if len(pre_list) == 1:
                return node
            i = 0
            while pre_list[1] != post_list[i]:
                i += 1
            node.right = func(pre_list[i+2:], post_list[i+1:])
            return node
        return func(pre, post)