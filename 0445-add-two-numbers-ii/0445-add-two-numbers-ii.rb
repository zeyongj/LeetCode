/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // make 2 stack
    let s1 = []
    let s2 = []
    while (l1){
        s1.push(l1.val)
        l1 = l1.next
    }
    while (l2){
        s2.push(l2.val)
        l2 = l2.next
    }
    
	// similiar to 2. Add Two Numbers
    let list = new ListNode(0)
    let sum = 0;
    
    while (s1.length !== 0 || s2.length !== 0 || sum > 0){
        sum = sum + (s1.length === 0? 0: s1.pop())
        sum = sum + (s2.length === 0? 0: s2.pop())
        // start to deal with linked list
		// update current node value
        list.val = sum % 10
		// add new head node with carry, head.val could be 1 or 0
		sum = Math.floor(sum/10);
        let head = new ListNode(sum)
		// connect
        head.next = list
		// update the head
        list = head
    }
    if (list.val === 0){
        return list.next
    } else {
        return list
    }
};