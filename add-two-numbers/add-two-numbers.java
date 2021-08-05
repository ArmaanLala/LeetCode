/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        boolean run = true;
        
        ListNode head = new ListNode();
        ListNode cur = head;
        int left = 0;
        int right = 0;
        int carry = 0;
        int sum = 0;
        while(run) {
            left = 0;
            right = 0;
            sum = 0;
            if (l1 == null && l2 == null) {
                return head;
            } else if (l2 == null) {
                left = l1.val;
                l1 = l1.next;
            } else if (l1 == null) {
                right = l2.val;
                l2 = l2.next;
            } else {
                right = l2.val;
                l2 = l2.next;
                left = l1.val;
                l1 = l1.next;
            }
            sum = left + right ;
            cur.val = cur.val + sum;
            carry = cur.val /10;
            cur.val = cur.val % 10;
            
            if (l1 == null && l2 == null && carry == 0) {
                return head;
            }
            cur.next = new ListNode(carry);
            cur = cur.next;
        }
        return head;
    }
}