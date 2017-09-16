# Definition for singly-linked list.
from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cur = ListNode(None)
        newHead = cur
        while l1 is not None or l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            if l1 is None:
                cur.next = l2
                break
            if l2 is None:
                cur.next = l1
                break
        return newHead.next

    def mergeKListsSecond(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None
        if len(lists) == 0:
            return []
        while len(lists) > 1:
            lists.append(self.mergeTwoLists(lists[0], lists[1]))
            lists = lists[1:]
            lists = lists[1:]
        return lists[0]

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None
        if len(lists) == 0:
            return []
        cur = ListNode()
        newHead = cur
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return newHead.next
