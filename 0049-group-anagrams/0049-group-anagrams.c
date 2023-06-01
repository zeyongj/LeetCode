#define MAX_WORD_LEN 101
#define MAX_GROUP_SIZE 10000
#define MAX_GROUP_NUM 10000

int cmpfunc (const void * a, const void * b) {
   return ( *(char*)a - *(char*)b );
}

unsigned long hash_func(char* str) {
    unsigned long hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c;
    return hash;
}

char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    char ***returnArray = (char ***)malloc(sizeof(char **) * MAX_GROUP_NUM);
    char **keys = (char **)malloc(sizeof(char *) * MAX_GROUP_NUM);
    int *groupSize = (int *)malloc(sizeof(int) * MAX_GROUP_NUM);
    unsigned long *hashArray = (unsigned long *)malloc(sizeof(unsigned long) * MAX_GROUP_NUM);
    char *sorted_str = (char *)malloc(sizeof(char) * MAX_WORD_LEN);
    int groupNum = 0;

    *returnColumnSizes = (int *)malloc(sizeof(int) * MAX_GROUP_NUM);

    for (int i = 0; i < strsSize; ++i) {
        int strLen = strlen(strs[i]);
        strncpy(sorted_str, strs[i], strLen + 1);
        qsort(sorted_str, strLen, sizeof(char), cmpfunc);
        unsigned long hash_val = hash_func(sorted_str);
        
        int j;
        for (j = 0; j < groupNum; ++j) {
            if (hash_val == hashArray[j]) {
                returnArray[j][groupSize[j]] = strs[i];
                (*returnColumnSizes)[j]++;
                groupSize[j]++;
                break;
            }
        }
        
        if (j == groupNum) {
            hashArray[groupNum] = hash_val;
            keys[groupNum] = sorted_str;
            returnArray[groupNum] = (char **)malloc(sizeof(char *) * MAX_GROUP_SIZE);
            returnArray[groupNum][0] = strs[i];
            groupSize[groupNum] = 1;
            (*returnColumnSizes)[groupNum] = 1;
            groupNum++;
        }
    }

    *returnSize = groupNum;
    return returnArray;
}
