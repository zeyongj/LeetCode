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
    public ListNode removeElements(ListNode head, int val) {
        if(head == null) 
            return null;
        ListNode curr = new ListNode(0), pre, now = head;
        curr.next = head; 
        pre = curr;
        while(now !=null){
            if(now.val == val) {
                pre.next = now.next; 
                now = now.next; 
            }
            else {
                pre = now; 
                now = now.next;}
        }
        return curr.next;
    }
}
