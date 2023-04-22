/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{-1, head}
    prev := dummy

    for head != nil && head.Next != nil {
        first_node := head
        second_node := head.Next

        // Swap the nodes
        prev.Next = second_node
        first_node.Next = second_node.Next
        second_node.Next = first_node

        // Move to the next pair
        prev = first_node
        head = first_node.Next
    }

    return dummy.Next
}