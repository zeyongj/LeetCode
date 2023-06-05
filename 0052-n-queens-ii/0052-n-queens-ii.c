typedef struct {
    int cell;   // cell is key
    UT_hash_handle hh;
} hElem;

typedef struct {
    hElem *cols;
    hElem *pDiag;
    hElem *nDiag;
    char **b;
} bData;

void backtrack(int r, int n, bData *o, int *res) {
    // found one valid board after placing N queens
    if(r == n) {   
        (*res)++;
        return;
    }    
    
    // try placing the queen in current in all columns of current row
    for(int c = 0; c < n; c++) {
        // cannot place the queen in same column or both diagonals if 
        // we have already placed previously
        hElem *tC, *tpD, *tnD;
        int pD = r + c;
        int nD = r - c;
        HASH_FIND_INT(o->cols, &c, tC);
        HASH_FIND_INT(o->pDiag, &pD, tpD);
        HASH_FIND_INT(o->nDiag, &nD, tnD);
        if(tC != NULL || tpD != NULL || tnD != NULL)  continue;
        
        // we can use this cell. update sets
        tC = calloc(sizeof(hElem), 1);
        tpD = calloc(sizeof(hElem), 1);
        tnD = calloc(sizeof(hElem), 1);
        tC->cell = c; tpD->cell = r + c; tnD->cell = r - c;
        HASH_ADD_INT(o->cols, cell, tC);
        HASH_ADD_INT(o->pDiag, cell, tpD);
        HASH_ADD_INT(o->nDiag, cell, tnD);
        
        // update board by placing queen in this cell
        o->b[r][c] = 'Q';
        backtrack(r+1, n, o, res);
        
        HASH_DEL(o->cols, tC);  free(tC);
        HASH_DEL(o->pDiag, tpD); free(tpD);
        HASH_DEL(o->nDiag, tnD); free(tnD);
        o->b[r][c] = '.';
    }
}

int totalNQueens(int n){
    // initialize board
    bData *obj = calloc(sizeof(bData), 1);
    obj->b = calloc(sizeof(char *), n);
    for(int i = 0; i < n; i++) {
        obj->b[i] = calloc(sizeof(char), n);
        memset(obj->b[i], '.', n);
    }
    
    // hash sets: columns, diagonal, anti diagonal cell values are stored
    // these sets are checked before placing the Queen
    obj->cols = NULL, obj->pDiag = NULL, obj->nDiag = NULL;
    int *res = 0;
    backtrack(0, n, obj, &res);
    return res;
}