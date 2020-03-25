class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res, pre = l1, l1
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            v = s % 10
            c = s // 10
            l1.val = v
            pre = l1
            l1, l2 = l1.next, l2.next
        if l2:
            pre.next = l2
            l1 = pre.next
        while l1:
            s = l1.val + c
            v = s % 10
            c = s // 10
            l1.val = v
            pre = l1
            l1 = l1.next
        if c:
            pre.next = ListNode(1)
        return res
