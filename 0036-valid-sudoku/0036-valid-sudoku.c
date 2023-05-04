#include <stdbool.h>

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    int rowCheck[9][9] = {0};
    int colCheck[9][9] = {0};
    int boxCheck[9][9] = {0};
    
    for(int i = 0; i < boardSize; i++) {
        for(int j = 0; j < boardColSize[i]; j++) {
            if(board[i][j] != '.') {
                int num = board[i][j] - '1'; // Subtract '1' to get index 0-8
                int k = (i / 3) * 3 + j / 3; // Identify which 3x3 box it is in
                if(rowCheck[i][num] || colCheck[j][num] || boxCheck[k][num])
                    return false;
                
                rowCheck[i][num] = 1;
                colCheck[j][num] = 1;
                boxCheck[k][num] = 1;
            }
        }
    }
    return true;
}
