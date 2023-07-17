/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
  import scala.collection.mutable
  import scala.math.Integral.Implicits._
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val s1 = new mutable.Stack[Int]()
    val s2 = new mutable.Stack[Int]()
    def reverseList(l1: ListNode, s1: mutable.Stack[Int]): mutable.Stack[Int] = l1 match {
      case null => s1
      case l1 => { s1.push(l1.x)
                   reverseList(l1.next, s1)}
    }
    reverseList(l1, s1)
    reverseList(l2, s2)

    def add(s1: mutable.Stack[Int], s2: mutable.Stack[Int], carry: Int, res: ListNode): ListNode = {
      if (s1.isEmpty && s2.isEmpty && carry == 0) return res
      val n1 = if (s1.nonEmpty) s1.pop() else 0
      val n2 = if (s2.nonEmpty) s2.pop() else 0
      val (q, r) = (carry + n1 + n2) /% 10
      if (res == null)  add(s1, s2, q, new ListNode(r))
      else add(s1, s2, q, new ListNode(r, res))
    }
    add(s1, s2, 0, null)
  }
}