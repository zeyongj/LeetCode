/*int min(int a,int b)
{
    return a>b?b:a;
}*/

int minPathSum(int** grid, int gridSize, int* gridColSize){
    int i,j;
    for(i=1;i<*gridColSize;i++)
    {
        grid[0][i]+=grid[0][i-1];
    }
    for(i=1;i<gridSize;i++)
    {
        grid[i][0]+=grid[i-1][0];
    }
    for(i=1;i<gridSize;i++)
    {
        for(j=1;j<*gridColSize;j++)
        {
            //grid[i][j]+=min(grid[i-1][j],grid[i][j-1]);
            grid[i][j]+=grid[i-1][j]>grid[i][j-1]?grid[i][j-1]:grid[i-1][j];
        }
    }
    return grid[gridSize-1][*gridColSize-1];
}