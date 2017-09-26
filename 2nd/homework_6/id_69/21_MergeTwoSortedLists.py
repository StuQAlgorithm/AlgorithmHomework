# https://leetcode.com/problems/merge-two-sorted-lists/description/
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        res = ListNode(None)
        d = res
        while(p1 and p2):
            if p1.val <= p2.val:
                d.next = p1
                p1 = p1.next
            else:
                d.next = p2
                p2 = p2.next
            d = d.next
        d.next = p2 if p1 is None else p1
        return res.next
