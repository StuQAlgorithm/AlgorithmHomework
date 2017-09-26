# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

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
        if head is None: return
        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None

if __name__ == '__main__':
    sol = Solution()
    l = [3,2,0,-4]
    n = ListNode(l.pop(0))
    d = n
    while l:
        n.next = ListNode(l.pop(0))
        n= n.next
    print(sol.detectCycle(d))
