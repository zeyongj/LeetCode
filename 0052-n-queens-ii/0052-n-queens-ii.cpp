class Solution {
public:
    int totalNQueens(int n) {
        vector<bool> col(n, false);
        vector<bool> antiDiag(2 * n - 1, false);  // Anti-diagonals
        vector<bool> mainDiag(2 * n - 1, false);  // Main diagonals
        return dfs(0, col, mainDiag, antiDiag);
    }

private:
    int dfs(int y, vector<bool>& col, vector<bool>& mainDiag, vector<bool>& antiDiag) {
        int n = col.size();
        if (y == n) {
            return 1;
        }
        int count = 0;
        for (int x = 0; x < n; x++) {
            if (col[x] || mainDiag[x + y] || antiDiag[x - y + n - 1]) {
                continue;
            }
            col[x] = mainDiag[x + y] = antiDiag[x - y + n - 1] = true;
            count += dfs(y + 1, col, mainDiag, antiDiag);
            col[x] = mainDiag[x + y] = antiDiag[x - y + n - 1] = false;
        }
        return count;
    }
};
