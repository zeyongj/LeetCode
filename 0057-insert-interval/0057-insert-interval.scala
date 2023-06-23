object Solution {
  def insert(intervals: Array[Array[Int]], newInterval: Array[Int]): Array[Array[Int]] = {
    val (acc, last) = intervals.foldLeft((Array.empty[Array[Int]], newInterval)) {
      case ((rest, newInterval), head) =>
        if (newInterval.last < head.head) {
          (rest :+ newInterval, head)
        } else if (newInterval.head > head.last) {
          (rest :+ head, newInterval)
        } else {
          (rest, Array(Math.min(head.head, newInterval.head), Math.max(head.last, newInterval.last)))
        }
    }
    acc :+ last
  }
}