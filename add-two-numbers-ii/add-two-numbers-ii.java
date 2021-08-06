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
        Deque<ListNode> stack1 = new ArrayDeque<>();
        Deque<ListNode> stack2 = new ArrayDeque<>();
        while (l1 != null || l2 != null) {
            if (l1 != null) {
                stack1.push(l1);
                l1 = l1.next;
            }
            if (l2 != null) {
                stack2.push(l2);
                l2 = l2. next;
            }
        }
        
        ListNode head = new ListNode();
        ListNode cur = head;
        int left = 0;
        int right = 0;
        int carry = 0;
        int sum = 0;
        while(!stack1.isEmpty() || !stack2.isEmpty()) {
            left = 0;
            right = 0;
            
            if (!stack1.isEmpty()) {
                left = stack1.pop().val;
            }
            if (!stack2.isEmpty()) {
                right = stack2.pop().val;
            }
            sum = left + right + cur.val;
            carry = sum /10;
            
            sum = sum %10;
            cur.val = sum;
            
            if (stack1.isEmpty() && stack2.isEmpty() && carry == 0) {
                head = reverseList(head);
                return head;
            }
            
            cur.next = new ListNode(carry);
            cur = cur.next;
            
        }
        head = reverseList(head);
        return head;
        
    }
    
    private ListNode reverseList(ListNode head) {
        
        ListNode prev = null;
        ListNode cur = head;
        ListNode next = null;
        
        while(cur != null) {
            next = cur.next;
            cur.next = prev;
            prev  = cur;
            cur = next;
        }
        
        return prev;
    }
}