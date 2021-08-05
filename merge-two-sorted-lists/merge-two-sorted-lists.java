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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head;
        ListNode cur;
        
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null) {
            return l2;
        } else if (l2 == null) {
           return l1; 
        }
        
        if (l1.val < l2.val ) {
            head = l1;
            l1 = l1.next;
            cur = head;
        } else {
            head = l2;
            l2 = l2.next;
            cur = head;
        }
        
        while (l1 != null || l2 != null){
            if (l1 == null) {
                System.out.println("l2 x : " + l2.val);
                cur.next = l2;
                l2 = l2.next;
                cur = cur.next;
            } else if (l2 == null) {
                System.out.println("l1 x: " + l1.val);
                cur.next = l1;
                l1 = l1.next;
                cur = cur.next;
            } else if (l2.val < l1.val) {
                System.out.println("l2 : " + l2.val);
                cur.next = l2;
                l2 = l2.next;
                cur = cur.next;
            } else {
                System.out.println("l1 : " + l1.val);
                cur.next = l1;
                l1 = l1.next;
                cur = cur.next;
            }
          
        }
        return head;
    }
}