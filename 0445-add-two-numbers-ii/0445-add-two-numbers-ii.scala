/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var stack1, stack2 []int
    for l1 != nil {
        stack1 = append(stack1, l1.Val)
        l1 = l1.Next
    }
    for l2 != nil {
        stack2 = append(stack2, l2.Val)
        l2 = l2.Next
    }
    var head *ListNode
    var over int
    for len(stack1) > 0 || len(stack2) > 0 || over > 0 {
        sum := over
        if len(stack1) > 0 {
            sum += stack1[len(stack1)-1]
            stack1 = stack1[:len(stack1)-1]
        }
        if len(stack2) > 0 {
            sum += stack2[len(stack2)-1]
            stack2 = stack2[:len(stack2)-1]
        }
        temp := ListNode{sum % 10, nil}
        over = sum / 10
        temp.Next = head
        head = &temp
    }
    return head
}