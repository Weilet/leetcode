# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []

        def dfs(root, level=0):
            if root:
                if len(ans) <= level:
                    ans.append([0, 0])
                ans[level][0] += root.val
                ans[level][1] += 1
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        dfs(root)
        return [s/float(c) for s, c in ans]