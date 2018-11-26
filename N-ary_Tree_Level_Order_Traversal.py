"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # ans = []
        #
        # def level(root, depth=0):
        #     if root:
        #         if len(ans) <= depth:
        #             ans.append([])
        #         ans[depth].append(root.val)
        #         for c in root.children:
        #             level(c, depth+1)
        # level(root)
        # return ans
        ans, q = [], root and [root]
        while q:
            tmp = []
            size = len(q)
            for _ in range(size):
                cur = q.pop(0)
                tmp.append(cur.val)
                for c in cur.children:
                    q.append(c)
            ans.append(tmp)
        return ans