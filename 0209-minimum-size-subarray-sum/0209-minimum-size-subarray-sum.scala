object Solution {
    
    def process(sums: Array[Int], left: Int, index: Int, min: Int, target: Int): Int = {
        if (index >= sums.length) min
        else if (sums(index) - sums(left) < target) {
             process(sums, left, index + 1, min, target)
        } else process(sums, left + 1, index, min.min(index - left), target)
    }
    
    def minSubArrayLen(target: Int, nums: Array[Int]): Int = {
        val sums = nums.scanLeft(0)(_ + _)
        val result = process(sums, left = 0, index = 0, Int.MaxValue, target)
        if (result == Int.MaxValue) 0 else result
    }
}