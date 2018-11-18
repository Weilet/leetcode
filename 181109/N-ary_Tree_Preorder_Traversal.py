class Solution(object):
    def preorder(self, root):
        ret, q = [], root and [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            q += [child for child in reversed(node.children) if child]
        return ret

