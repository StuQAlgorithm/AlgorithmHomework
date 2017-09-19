# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        fast, slow, entr = head, head, head

        while (fast.next and fast.next.next and slow.next):
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                while(slow != entr):
                    slow = slow.next
                    entr = entr.next
                return entr

        return None
