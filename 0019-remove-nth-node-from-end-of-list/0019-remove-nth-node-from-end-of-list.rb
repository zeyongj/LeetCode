# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  dummy = ListNode.new(0, head)
  first = dummy
  second = dummy

  # Move first pointer n nodes ahead in the linked list
  (n + 1).times do
    first = first.next
  end

  # Move first to the end, maintaining the gap
  while first
    first = first.next
    second = second.next
  end

  # Skip the desired node
  second.next = second.next.next

  # Return the new head node
  dummy.next
end