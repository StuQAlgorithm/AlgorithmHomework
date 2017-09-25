# https://leetcode.com/problems/merge-k-sorted-lists/description/
import heapq


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        cur = dummy
        queue = []
        for n in lists:
            if n:
                heapq.heappush(queue, (n.val, n))
        while queue:
            cur.next = heapq.heappop(queue)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(queue, (cur.next.val, cur.next))
        return dummy.next
