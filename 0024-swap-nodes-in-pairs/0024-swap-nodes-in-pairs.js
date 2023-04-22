/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    let dummy = new ListNode(-1);
    dummy.next = head;
    let prev = dummy;
    
    while (head && head.next) {
        let first_node = head;
        let second_node = head.next;

        // Swap the nodes
        prev.next = second_node;
        first_node.next = second_node.next;
        second_node.next = first_node;

        // Move to the next pair
        prev = first_node;
        head = first_node.next;
    }

    return dummy.next;
};
