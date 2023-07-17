/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let a1 = [], a2 = [], current = null, last = null, carry = 0, subSum = 0;
    
    for (let pl1 = l1; pl1 != null; pl1 = pl1.next) a1.push(pl1.val);
    for (let pl2 = l2; pl2 != null; pl2 = pl2.next) a2.push(pl2.val);
    
    for (let i = a1.length - 1, j = a2.length - 1; i >= 0 || j >= 0 || carry; i--, j--) {
        subSum = carry;
        if (i >= 0) subSum += a1[i];
        if (j >= 0) subSum += a2[j];
        
        current = new ListNode(subSum % 10);
        if (last != null) current.next = last;
        last = current;
        
        carry = Math.floor(subSum / 10);
    }
    return last;
};