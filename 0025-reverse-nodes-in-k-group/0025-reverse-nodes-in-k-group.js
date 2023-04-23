/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    if (!head || k === 1) {
        return head;
    }

    let dummy = new ListNode(0, head);
    let prev = dummy;
    let tail = dummy;
    let curr = head;

    let length = 0;
    while (curr) {
        length++;
        curr = curr.next;
    }

    while (length >= k) {
        curr = prev.next;
        tail = prev;
        for (let i = 0; i < k; ++i) {
            tail = tail.next;
        }
        let nextGroupStart = tail.next;
        tail.next = null;

        prev.next = reverseList(curr);
        curr.next = nextGroupStart;
        prev = curr;

        length -= k;
    }

    return dummy.next;
};

function reverseList(head) {
    let prev = null;
    let curr = head;

    while (curr) {
        let nextNode = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextNode;
    }

    return prev;
}
