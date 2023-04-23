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
    public ListNode reverseKGroup(ListNode head, int k) {
        if ((head == null) || k == 1) {
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        ListNode tail = dummy;
        ListNode curr = head;

        int len = 0;
        while (curr != null) {
            len++;
            curr = curr.next;
        }

        while (len >= k) {
            curr = prev.next;
            tail = prev;
            for (int i = 0; i < k; ++i) {
                tail = tail.next;
            }
            ListNode next_group_start = tail.next;
            tail.next = null;

            prev.next = reverseList(curr);
            curr.next = next_group_start;
            prev = curr;

            len -= k;
        }

        return dummy.next;
    }

    ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};