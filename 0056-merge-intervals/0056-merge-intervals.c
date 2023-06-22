int cmpfunc(int** a, int** b)
{
    return (*a)[0] - (*b)[0];
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes){
    int* temp=NULL;
    int i;
    int count = 0;
    
    if((intervals==NULL) || (intervalsSize==0))
    {
        *returnSize = 0;
        return NULL;
    }
    qsort(intervals, intervalsSize,sizeof(int*),cmpfunc);
    
    temp = intervals[0];
    for(i=1;i<intervalsSize;i++)
    {
        if(temp[1] >= intervals[i][0])
        {
            temp[1] = (temp[1] > intervals[i][1])?temp[1]:intervals[i][1];
        }
        else
        {
            intervals[count][0] = temp[0];
            intervals[count][1] = temp[1];
            count++;
            temp = intervals[i];
        }
    }
    intervals[count][0] = temp[0];
    intervals[count][1] = temp[1];
    count++;

    *returnSize = count;
    (*returnColumnSizes) = (int*)malloc(count*sizeof(int));
    for(i=0;i<count;i++)
    {
        (*returnColumnSizes)[i] = 2;
    }
    return intervals;
}