/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func getReverse(_ node: ListNode?) -> ListNode? {
        var temp: ListNode? = nil
        var pre: ListNode? = nil
        var head = node
        var current = node
        
        while(current != nil) {
            temp = current?.next
            current?.next = pre
            pre = current
            current = temp
        }
        head = pre
        return head
    }
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var revL1 = getReverse(l1)
        var revL2 = getReverse(l2)
        var res : ListNode? = nil
        var carry = 0
        while(revL1 != nil || revL2 != nil || carry != 0) {
            var sum = 0
            if revL1 != nil {
                sum += revL1?.val ?? 0
                revL1 = revL1?.next
            }
            if revL2 != nil {
                sum += revL2?.val ?? 0
                revL2 = revL2?.next
            }
            let newNode = ListNode(((carry + sum) % 10))
            newNode.next = res
            res = newNode
            carry = (carry + sum) / 10
        }
        return res
    }
}