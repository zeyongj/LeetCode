int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int* list = malloc(sizeof(int)*(*obstacleGridColSize));
    for (int i = 0 ; i < *obstacleGridColSize ; i++){
        if (obstacleGrid[0][i] == 1){
            list[i] = 0;
            i++;
            while (i < *obstacleGridColSize){
                list[i] = 0;
                i++;
            } 
        } else {
            list[i] = 1;
        }
    }
    for (int i = 1 ; i < obstacleGridSize ; i++){
        if (obstacleGrid[i][0] == 1){
            list[0] = 0;
        }
        for (int j = 1 ; j < *obstacleGridColSize ; j++){
            if (obstacleGrid[i][j] == 1){
                list[j] = 0;
            } else {
                list[j] += list[j-1];
            }
        }
    }
    int ans = list[*obstacleGridColSize-1];
    free(list);
    return ans < 2000000000 ? ans : 2000000000;
}