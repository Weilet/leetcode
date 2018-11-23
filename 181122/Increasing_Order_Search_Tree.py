# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def travel(root):
            if not root:
                return []
            else:
                return travel(root.left) + [root.val] + travel(root.right)
        forest = travel(root)
        ans = pos = TreeNode(None)
        for tree in forest:
            pos.right = TreeNode(tree)
            pos = pos.right
        return ans.right

#  TODO: shorten the code