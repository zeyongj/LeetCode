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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prev = dummy;
        
        while ((head != null) && (head.next != null)){
            ListNode first_node = head;
            ListNode second_node = head.next;
            
            prev.next = second_node;
            first_node.next = second_node.next;
            second_node.next = first_node;
            
            prev = first_node;
            head = first_node.next;
        }
        return dummy.next;
    }
}