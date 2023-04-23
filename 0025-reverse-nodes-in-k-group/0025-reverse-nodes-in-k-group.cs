// Definition for singly-linked list.
// public class ListNode {
//     public int val;
//     public ListNode next;
//     public ListNode(int val = 0, ListNode next = null) {
//         this.val = val;
//         this.next = next;
//     }
// }

public class Solution {
    public ListNode ReverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) {
            return head;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        ListNode tail = dummy;
        ListNode curr = head;

        int length = 0;
        while (curr != null) {
            length++;
            curr = curr.next;
        }

        while (length >= k) {
            curr = prev.next;
            tail = prev;
            for (int i = 0; i < k; ++i) {
                tail = tail.next;
            }
            ListNode nextGroupStart = tail.next;
            tail.next = null;

            prev.next = ReverseList(curr);
            curr.next = nextGroupStart;
            prev = curr;

            length -= k;
        }

        return dummy.next;
    }

    private ListNode ReverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        return prev;
    }
}
