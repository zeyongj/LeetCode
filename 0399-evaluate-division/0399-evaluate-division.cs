public class Solution {
    private Dictionary<string, Dictionary<string, double>> graph = new Dictionary<string, Dictionary<string, double>>();
    
    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) {
        for (int i = 0; i < equations.Count; i++) {
            var equation = equations[i];
            if (!graph.ContainsKey(equation[0])) {
                graph[equation[0]] = new Dictionary<string, double>();
            }
            if (!graph.ContainsKey(equation[1])) {
                graph[equation[1]] = new Dictionary<string, double>();
            }
            graph[equation[0]][equation[1]] = values[i];
            graph[equation[1]][equation[0]] = 1 / values[i];
        }
        
        double[] result = new double[queries.Count];
        for (int i = 0; i < queries.Count; i++) {
            var query = queries[i];
            result[i] = DFS(query[0], query[1], new HashSet<string>());
        }
        return result;
    }
    
    private double DFS(string start, string end, HashSet<string> visited) {
        if (!graph.ContainsKey(start)) return -1.0;
        if (graph[start].ContainsKey(end)) return graph[start][end];
        
        visited.Add(start);
        foreach (var neighbor in graph[start].Keys) {
            if (!visited.Contains(neighbor)) {
                double productWeight = DFS(neighbor, end, visited);
                if (productWeight != -1) return graph[start][neighbor] * productWeight;
            }
        }
        return -1.0;
    }
}
