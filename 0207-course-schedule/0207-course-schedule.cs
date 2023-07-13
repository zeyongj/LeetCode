public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites == null || prerequisites.Length == 0)
            return true;
        
        List<int>[] g = new List<int>[numCourses];
        int[] indegree = new int[numCourses];
        Queue<int> q = new Queue<int>();
        int nodeCount = 0;
        
        foreach (var item in prerequisites)
        {
            if (g[item[0]] == null)
                g[item[0]] = new List<int>();
            
            g[item[0]].Add(item[1]);
            indegree[item[1]] += 1;
        }
        
        for (int i = 0; i < numCourses; i++)
            if (indegree[i] == 0)
                q.Enqueue(i);
        
        while (q.Count > 0)
        {
            int cur = q.Dequeue();
            
            if (g[cur] != null)            
                foreach (var item in g[cur])
                    if (--indegree[item] == 0)
                        q.Enqueue(item);
            
            nodeCount++;
        }
        
        return nodeCount == numCourses;
    }
}