#include <vector>
#include <set>
#include <string>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::set<std::string> seen;
        
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char number = board[i][j];
                if (number != '.') {
                    std::string row = std::to_string(number) + " seen in row " + std::to_string(i);
                    std::string col = std::to_string(number) + " seen in col " + std::to_string(j);
                    std::string box = std::to_string(number) + " seen in box " + std::to_string(i / 3) + "-" + std::to_string(j / 3);

                    if (seen.find(row) != seen.end() || seen.find(col) != seen.end() || seen.find(box) != seen.end()) {
                        return false;
                    }
                    
                    seen.insert(row);
                    seen.insert(col);
                    seen.insert(box);
                }
            }
        }
        
        return true;
    }
};
