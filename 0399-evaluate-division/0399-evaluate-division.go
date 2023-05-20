type Graph map[string]map[string]float64

func (g Graph) AddEdge(from string, to string, value float64) {
    if _, ok := g[from]; !ok {
        g[from] = make(map[string]float64)
    }
    g[from][to] = value
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    g := make(Graph)
    for i, e := range equations {
        g.AddEdge(e[0], e[1], values[i])
        g.AddEdge(e[1], e[0], 1/values[i])
    }
    res := make([]float64, len(queries))
    for i, q := range queries {
        res[i] = g.DFS(q[0], q[1], map[string]bool{})
    }
    return res
}

func (g Graph) DFS(from string, to string, visited map[string]bool) float64 {
    if _, ok := g[from]; !ok {
        return -1.0
    }
    if from == to {
        return 1.0
    }
    visited[from] = true
    for neighbor, value := range g[from] {
        if visited[neighbor] {
            continue
        }
        temp := g.DFS(neighbor, to, visited)
        if temp > 0 {
            return temp * value
        }
    }
    return -1.0
}
