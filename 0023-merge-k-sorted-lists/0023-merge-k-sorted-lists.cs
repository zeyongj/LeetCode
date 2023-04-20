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
using System;
using System.Collections.Generic;
public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        var set = new SortedSet<(int val, int idx, ListNode node)>(
            Comparer<(int val, int idx, ListNode node)>.Create((a, b) => {
                int result = a.val.CompareTo(b.val);
                return result != 0 ? result : a.idx.CompareTo(b.idx);
            }));

        for (int i = 0; i < lists.Length; i++) {
            ListNode head = lists[i];
            if (head != null) {
                set.Add((head.val, i, head));
            }
        }

        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (set.Count > 0) {
            var item = set.Min;
            set.Remove(item);

            tail.next = item.node;
            tail = tail.next;

            if (item.node.next != null) {
                set.Add((item.node.next.val, item.idx, item.node.next));
            }
        }

        return dummy.next;
    }
}