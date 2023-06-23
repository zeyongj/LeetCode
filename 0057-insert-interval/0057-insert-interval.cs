/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes){
  *returnSize = 0;
  int head = newInterval[0], end = newInterval[1], idx, inserted = 0;
  int **result = (int**)malloc(sizeof(int*) * (intervalsSize + 1));
  *returnColumnSizes = (int*)malloc(sizeof(int) * (intervalsSize + 1));
  for(idx = 0; idx < intervalsSize; idx++){   
    if (head > intervals[idx][1]){
      result[*returnSize] = (int*)malloc(sizeof(int) * 2);
      result[*returnSize][0] = intervals[idx][0];
      result[*returnSize][1] = intervals[idx][1];
      (*returnColumnSizes)[*returnSize] = 2;
      (*returnSize)++;
    }
    else{ 
      if (head > intervals[idx][0]) head = intervals[idx][0];      
      if (end < intervals[idx][0]){        
        result[*returnSize] = (int*)malloc(sizeof(int) * 2);
        result[*returnSize][0] = head;
        result[*returnSize][1] = end;
        (*returnColumnSizes)[*returnSize] = 2;
        (*returnSize)++;
        inserted = 1;
        break;
      }
      else if (end < intervals[idx][1]) end = intervals[idx][1];
    }
  }
  
  if(!inserted) {
    result[*returnSize] = (int*)malloc(sizeof(int) * 2);
    result[*returnSize][0] = head;
    result[*returnSize][1] = end;
    (*returnColumnSizes)[*returnSize] = 2;
    (*returnSize)++;    
    return result;
  }
  
  while(idx < intervalsSize){
    result[*returnSize] = (int*)malloc(sizeof(int) * 2);
    result[*returnSize][0] = intervals[idx][0];
    result[*returnSize][1] = intervals[idx][1];
    (*returnColumnSizes)[*returnSize] = 2;
    (*returnSize)++;    
    idx++;
  }
  return result;
}