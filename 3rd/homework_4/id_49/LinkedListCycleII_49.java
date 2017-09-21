/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedListCycleII_49 {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        boolean hasCycle = false;
        ListNode first = head, second = head;
        while (second.next != null && second.next.next != null) {
            first = first.next;
            second = second.next.next;
            if (first == second) {
                hasCycle = true;
                break;
            }
        }
        if (!hasCycle) {
            return null;
        }
        first = head;
        while (first != second) {
            first = first.next;
            second = second.next;
        }
        return first;
    }
}