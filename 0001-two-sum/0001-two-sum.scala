object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val dict = scala.collection.mutable.Map[Int, Int]()
        for {
            pair @ (x, i) <- nums.zipWithIndex
            if dict.contains(target - x) || {dict += pair; false}
            j <- dict.get(target-x)
        } return Array(j,i)
        throw new IllegalArgumentException("No two sum solution");
    }
}