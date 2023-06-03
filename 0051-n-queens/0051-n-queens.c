void mark(int n, int** checkerboard, int i, int j){
    int left = j;
    int right = j;
    i++;
    right++;
    left--;
    while (i < n){
        if (right < n){
            checkerboard[i][right]++;
            right++;
        }
        if (left >= 0){
            checkerboard[i][left]++;
            left--;
        }
        checkerboard[i][j]++;
        i++;
    }
    return;
}

void del_mark(int n, int** checkerboard, int i, int j){
    int left = j;
    int right = j;
    i++;
    right++;
    left--;
    while (i < n){
        if (right < n){
            checkerboard[i][right]--;
            right++;
        }
        if (left >= 0){
            checkerboard[i][left]--;
            left--;
        }
        checkerboard[i][j]--;
        i++;
    }
    return;
}

void check(int** checkerboard, int n, int* returnSize, int i, char*** ans, int** returnColumnSizes, int* location){
    if (i == n){
        ans[*returnSize] = malloc(sizeof(char*)*n);
        for (int k = 0 ; k < n ; k++){
            ans[*returnSize][k] = malloc(sizeof(char)*(n+1));
            for (int t = 0 ; t < n ; t++){
                if (t == location[k]){
                    ans[*returnSize][k][t] = 'Q';
                } else ans[*returnSize][k][t] = '.';
            }
            ans[*returnSize][k][n] = '\0';
        }
        (*returnColumnSizes)[*returnSize] = n;
        *returnSize += 1;
        return;
    }
    for (int j = 0 ; j < n ; j++){
        if (checkerboard[i][j] == 0){
            mark( n, checkerboard, i, j);
            location[i] = j;
            check(checkerboard, n, returnSize, i+1, ans, returnColumnSizes, location);
            del_mark( n, checkerboard, i, j);
        } 
    }
}

char *** solveNQueens(int n, int* returnSize, int** returnColumnSizes){
    char*** ans = malloc(sizeof(char**)*352);
    (*returnColumnSizes) = malloc(sizeof(int)*352);
    int location[10];
    int** checkerboard = malloc(sizeof(int*)*n);
    for (int i = 0 ; i < n ; i++){
        checkerboard[i] = calloc(n,sizeof(int));
    }
    *returnSize = 0;
    check(checkerboard, n, returnSize, 0, ans, returnColumnSizes, location);
    for (int i = 0 ; i < n ; i++){
        free(checkerboard[i]);
    }
    free(checkerboard);
    return ans;
}