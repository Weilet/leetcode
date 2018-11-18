# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans[len(ans) // 2:]
#  TODO: Shorten the code
