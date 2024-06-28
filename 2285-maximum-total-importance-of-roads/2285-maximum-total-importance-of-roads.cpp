class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        long res = 0, cost = 1;
        vector<int> conn(n, 0);
        for (auto road : roads) {
            conn[road[0]]++;
            conn[road[1]]++;
        }
        sort(conn.begin(), conn.end());
        for (auto con : conn) res += con * (cost++);
        return res;
    }
};