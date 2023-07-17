# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    r = ''
    s = ''
    while l1
        r += l1.val.to_s
        l1 = l1.next
    end
    while l2
        s += l2.val.to_s
        l2 = l2.next
    end
    r = (r.to_i+s.to_i).to_s.chars.map(&:to_i).map {|x| ListNode.new(x)}.to_a
    for i in (1..r.length)
        r[i-1].next = r[i]
    end
    r[0]
end