import java.util.*;

class Solution {
    private HashMap<String, HashMap<String, Double>> graph = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // Construct the graph from the equations
        for (int i = 0; i < equations.size(); i++) {
            String num = equations.get(i).get(0);
            String den = equations.get(i).get(1);
            double val = values[i];
            graph.computeIfAbsent(num, k -> new HashMap<>()).put(den, val);
            graph.computeIfAbsent(den, k -> new HashMap<>()).put(num, 1.0 / val);
        }

        // Handle the queries
        double[] result = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String num = queries.get(i).get(0);
            String den = queries.get(i).get(1);
            if (!graph.containsKey(num) || !graph.containsKey(den)) {
                result[i] = -1.0;
            } else {
                HashSet<String> visited = new HashSet<>();
                result[i] = dfs(num, den, 1.0, visited);
            }
        }

        return result;
    }

    private double dfs(String start, String end, double product, Set<String> visited) {
        // If we've visited the node before, return -1.0
        if (visited.contains(start)) {
            return -1.0;
        }
        // If we've reached our destination, return the product
        if (start.equals(end)) {
            return product;
        }
        visited.add(start);

        // Continue DFS on all neighbours
        for (String neighbor : graph.get(start).keySet()) {
            double result = dfs(neighbor, end, product * graph.get(start).get(neighbor), visited);
            if (result != -1.0) {
                return result;
            }
        }

        return -1.0;
    }
}
