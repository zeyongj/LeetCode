// Definition for singly-linked list.
// type ListNode struct {
//     Val  int
//     Next *ListNode
// }

func reverseKGroup(head *ListNode, k int) *ListNode {
    if head == nil || k == 1 {
        return head
    }

    dummy := &ListNode{0, head}
    prev := dummy
    tail := dummy
    curr := head

    length := 0
    for curr != nil {
        length++
        curr = curr.Next
    }

    for length >= k {
        curr = prev.Next
        tail = prev
        for i := 0; i < k; i++ {
            tail = tail.Next
        }
        nextGroupStart := tail.Next
        tail.Next = nil

        prev.Next = reverseList(curr)
        curr.Next = nextGroupStart
        prev = curr

        length -= k
    }

    return dummy.Next
}

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    curr := head

    for curr != nil {
        nextNode := curr.Next
        curr.Next = prev
        prev = curr
        curr = nextNode
    }

    return prev
}
