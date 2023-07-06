class Solution {
    fun minSubArrayLen(target: Int, nums: IntArray): Int {
        var lo = 0
        var sum = 0
        return nums.asSequence().mapIndexed { hi, n ->
          sum += n
          while (sum - nums[lo] >= target) sum -= nums[lo++]
          (hi - lo + 1).takeIf { sum >= target }
        }
        .filterNotNull()
        .min() ?: 0
    }
}