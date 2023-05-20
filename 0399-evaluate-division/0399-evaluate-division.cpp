#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

class Solution {
public:
    unordered_map<string, unordered_map<string, double>> g;
    
    double dfs(string start, string end, unordered_map<string, int>& visited) {
        if(g.find(start) == g.end() || visited[start]) 
            return -1.0;
        if(start == end) 
            return 1.0;
        
        visited[start] = 1;
        for(auto [node, weight]: g[start]) {
            double tmp = dfs(node, end, visited);
            if(tmp != -1.0) 
                return tmp * weight;
        }
        
        return -1.0;
    }

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        for(int i = 0; i < equations.size(); i++) {
            string num = equations[i][0];
            string den = equations[i][1];
            double val = values[i];
            g[num][den] = val;
            g[den][num] = 1.0 / val;
        }

        vector<double> result;
        for(auto& q : queries) {
            string num = q[0];
            string den = q[1];
            unordered_map<string, int> visited;
            double tmp = dfs(num, den, visited);
            if(tmp != -1.0) 
                result.push_back(tmp);
            else 
                result.push_back(-1.0);
        }

        return result;
    }
};
