#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        vector<bool> onpath(numCourses, false), visited(numCourses, false);
        for(int i = 0; i < numCourses; i++) {
            if(!visited[i] && dfs_cycle(graph, i, onpath, visited))
                return false;
        }
        return true;
    }
private:
    vector<unordered_set<int>> make_graph(int numCourses, vector<vector<int>>& prerequisites){
        vector<unordered_set<int>> graph(numCourses);
        for(auto pre : prerequisites)
            graph[pre[1]].insert(pre[0]);
        return graph;
    }
    
    bool dfs_cycle(vector<unordered_set<int>>& graph, int node, vector<bool>& onpath, vector<bool>& visited){
        if(visited[node])
            return false;
        onpath[node] = visited[node] = true;
        for(int neigh : graph[node])
            if(onpath[neigh] || dfs_cycle(graph, neigh, onpath, visited))
                return true;
        return onpath[node] = false;
    }
};
