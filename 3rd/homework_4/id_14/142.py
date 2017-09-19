"""
Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
"""
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
        runner = head
        walker = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                node = head
                while node != walker:
                    walker = walker.next
                    node = node.next
                return node
        return None

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        nodeSet = set()
        while node:
            if node in nodeSet:
                return node
            nodeSet.add(node)
            node = node.next
        return None

head = ListNode(3)
head.next = ListNode(2)
node = head.next
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = node

s = Solution()
l = s.detectCycle(head)
if l:
    print(l.val)
else:
    print('Null')
