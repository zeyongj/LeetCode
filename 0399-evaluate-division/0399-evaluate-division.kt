class Solution {
    private val graph = mutableMapOf<String, MutableMap<String, Double>>()

    fun calcEquation(equations: List<List<String>>, values: DoubleArray, queries: List<List<String>>): DoubleArray {
        for (i in equations.indices) {
            val equation = equations[i]
            graph.getOrPut(equation[0], { mutableMapOf() })[equation[1]] = values[i]
            graph.getOrPut(equation[1], { mutableMapOf() })[equation[0]] = 1.0 / values[i]
        }

        val result = DoubleArray(queries.size)
        for (i in queries.indices) {
            result[i] = dfs(queries[i][0], queries[i][1], HashSet())
        }
        return result
    }

    private fun dfs(start: String, end: String, visited: HashSet<String>): Double {
        if (!graph.containsKey(start)) return -1.0
        if (graph[start]!!.containsKey(end)) return graph[start]!![end]!!

        visited.add(start)
        for ((neighbor, value) in graph[start]!!) {
            if (visited.contains(neighbor)) continue
            val product = dfs(neighbor, end, visited)
            if (product != -1.0) return value * product
        }
        return -1.0
    }
}
