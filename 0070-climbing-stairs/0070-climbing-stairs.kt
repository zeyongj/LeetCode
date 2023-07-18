import kotlin.math.sqrt
import kotlin.math.pow
import kotlin.math.round

class Solution {
    fun climbStairs(n: Int) = sqrt(5.0)?.let { round(((1.0 + it)/2.0).pow(n + 1.0)/it).toInt() }
}