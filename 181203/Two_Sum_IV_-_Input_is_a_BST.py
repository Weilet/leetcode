# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        ans = []
        def travel(t):
            if not t:
                if k - t.val in ans:
                    return True
                else:
                    ans.append(t.val)
                    travel(t.left)
                    travel(t.right)

        if travel(root):
            return True
        else:
            return False