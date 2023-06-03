#include<vector>
#include<string>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<int> queens(n, -1);
        solve(0, queens, result);
        return result;
    }
    
private:
    void solve(int row, vector<int>& queens, vector<vector<string>>& result) {
        int n = queens.size();
        if (row == n) {
            result.push_back(toBoard(queens));
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(row, col, queens)) {
                queens[row] = col;
                solve(row + 1, queens, result);
                queens[row] = -1;
            }
        }
    }
    
    bool isValid(int row, int col, vector<int>& queens) {
        for (int i = 0; i < row; i++) {
            if (queens[i] == col || queens[i] - i == col - row || queens[i] + i == col + row) {
                return false;
            }
        }
        return true;
    }
    
    vector<string> toBoard(vector<int>& queens) {
        int n = queens.size();
        vector<string> board(n, string(n, '.'));
        for (int i = 0; i < n; i++) {
            board[i][queens[i]] = 'Q';
        }
        return board;
    }
};
