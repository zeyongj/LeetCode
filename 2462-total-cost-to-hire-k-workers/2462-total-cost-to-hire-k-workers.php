class Solution {
    fun totalCost(costs: IntArray, k: Int, candidates: Int): Long {
        val pqL = PriorityQueue<Int>()
        val pqR = PriorityQueue<Int>()
        var lo = 0
        var hi = costs.lastIndex
        var sum = 0L
        var count = 0
        if (2 * candidates >= costs.size) while (lo <= hi) pqL.add(costs[lo++])
        while (pqL.size < candidates && lo <= hi) pqL.add(costs[lo++])
        while (pqR.size < candidates && lo < hi) pqR.add(costs[hi--])
        while (lo <= hi && count++ < k) {
            if (pqR.peek() < pqL.peek()) {
                sum += pqR.poll()
                pqR.add(costs[hi--])
            } else {
                sum += pqL.poll()
                pqL.add(costs[lo++])
            }
        }
        while (pqR.isNotEmpty()) pqL.add(pqR.poll())
        while (count++ < k && pqL.isNotEmpty()) sum += pqL.poll()
        return sum
    }
}