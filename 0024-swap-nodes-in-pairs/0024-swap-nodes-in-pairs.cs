/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prev = dummy;
        
        while (head != null && head.next != null) {
            ListNode first_node = head;
            ListNode second_node = head.next;
            
            // Swap the nodes
            prev.next = second_node;
            first_node.next = second_node.next;
            second_node.next = first_node;
            
            // Move to the next pair
            prev = first_node;
            head = first_node.next;
        }
        
        return dummy.next;
    }
}