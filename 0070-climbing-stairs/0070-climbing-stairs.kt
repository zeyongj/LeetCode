object Solution {
  def climbStairs(n: Int): Int = {
    def fib(a: Int, b: Int): Stream[Int] = {
      a #:: fib(b, a + b)
    }
    fib(1, 2).take(n).last
  }
}