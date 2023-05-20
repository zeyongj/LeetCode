/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    const graph = new Map();
    
    // Build the graph
    for (let i = 0; i < equations.length; i++) {
        const [start, end] = equations[i];
        const value = values[i];
        
        if (!graph.has(start)) graph.set(start, {});
        if (!graph.has(end)) graph.set(end, {});
        
        graph.get(start)[end] = value;
        graph.get(end)[start] = 1 / value;
    }
    
    // Function for DFS
    const dfs = function(node, target, visited) {
        // If the node does not exist in the graph, return -1.0
        if (!graph.has(node)) return -1.0;
        // If the node is the target, return 1.0
        if (node === target) return 1.0;
        
        visited.add(node);
        
        const neighbors = graph.get(node);
        for (let nextNode in neighbors) {
            if (visited.has(nextNode)) continue;
            const product = dfs(nextNode, target, visited);
            
            if (product === -1.0) continue;
            
            return neighbors[nextNode] * product;
        }
        
        return -1.0;
    };
    
    // Run queries through DFS
    const results = [];
    for (let query of queries) {
        const [start, end] = query;
        results.push(dfs(start, end, new Set()));
    }
    
    return results;
};
