/**
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode p = head;
        int sum = 0;

        while(l1 != null || l2 != null || sum > 0){
            sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + sum;

            ListNode cur = new ListNode(sum % 10);
            sum = sum / 10;

            p.next = cur;
            p = cur;

            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }

        return head.next;
    }
}