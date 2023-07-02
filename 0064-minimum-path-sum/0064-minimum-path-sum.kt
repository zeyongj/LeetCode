object Solution {
  def minPathSum(grid: Array[Array[Int]]): Int = {
    (grid.length, grid.headOption.map(_.length).getOrElse(0)) match {
      case (m, n) if m > 0 && n > 0 =>
        val dp = Array.fill(m, n)(grid(m - 1)(n - 1))
        for {
          k <- 1 to m + n
          i <- math.max(0, (m - 1) - k) to math.min(m - 1, m + n - k - 2)
        } {
          val j = m + n - i - k - 2
          dp(i)(j) = grid(i)(j) + Seq((i + 1, j), (i, j + 1))
            .collect {
              case (x, y) if dp.isDefinedAt(x) && dp(x).isDefinedAt(y) => dp(x)(y)
            }
            .min
        }
        dp(0)(0)
    }
  }
}