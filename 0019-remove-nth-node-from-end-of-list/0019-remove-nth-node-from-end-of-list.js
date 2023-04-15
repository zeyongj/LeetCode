/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0, head);
    let first = dummy;
    let second = dummy;

    // Move first pointer n nodes ahead in the linked list
    for (let i = 0; i < n + 1; i++) {
        first = first.next;
    }

    // Move first to the end, maintaining the gap
    while (first !== null) {
        first = first.next;
        second = second.next;
    }

    // Skip the desired node
    second.next = second.next.next;

    // Return the new head node
    return dummy.next;
};