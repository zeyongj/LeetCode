typedef struct _node{
    int val ;
    int idx ;
}node ;

int cmp(const void* a, const void* b){
    node *A = *(node**)a ;
    node *B = *(node**)b ;
    return A->val - B->val ;
}
void swap(node** a, node** b){
    node* tmp = *a ;
    *a = *b ;
    *b = tmp ;
}
void modifyHeap(node** heap, int n){
    int f =  0 ;
    while(1){
        int son1 = 2*f + 1 ;
        int son2 = 2*f + 2 ;
        if(son2 < n){
            if(heap[son1]->val <= heap[son2]->val){
                if(heap[son1]->val < heap[f]->val){
                    swap( &heap[f], &heap[son1] ) ;
                    f = son1 ;
                }
                else
                    break ;
            }
            else{
                if(heap[son2]->val < heap[f]->val){
                    swap( &heap[f], &heap[son2] ) ;
                    f = son2 ;
                }
                else
                    break ;
            }
        }
        else if(son1 < n){
            if(heap[son1]->val < heap[f]->val){
                swap( &heap[f], &heap[son1] ) ;
                f = son1 ;
            }
            else
                break ;
        }
        else
            break ;
    }
}
int heapPop(node** heap, int* n){
    int ans = heap[0]->val ;
    *n = *n - 1 ;
    heap[0] = heap[*n] ;
    
    int f = 0 ;
    int N = *n ;
    while(1){
        int son1 = 2*f + 1 ;
        int son2 = 2*f + 2 ;
            if(son2 < N){
                if(heap[son1]->val <= heap[son2]->val){
                    if(heap[f]->val > heap[son1]->val){
                        swap( &heap[f], &heap[son1] ) ;
                        f = son1 ;
                        continue ;
                    }
                    else
                        break ;
                }
                else{
                    if(heap[f]->val > heap[son2]->val){
                        swap( &heap[f], &heap[son2] ) ;
                        f = son2 ;
                        continue ;
                    }
                    else
                        break ;                    
                }
            }
            else if(son1 < N){
                if(heap[f]->val > heap[son1]->val){
                    swap( &heap[f], &heap[son1] ) ;
                    f = son1 ;
                    continue ;
                }
                else
                    break ;                
            }
            else
                break ;
        
    }
    return ans ;
}
long long totalCost(int* costs, int costsSize, int k, int candidates){    
    int n = costsSize ;
    int left_cn = candidates ;
    int right_cn = candidates ;    
    
    if((left_cn + right_cn) > n){
        left_cn = n/2 ;
        right_cn = n - n/2 ;
    }
    
    long long ans =  0 ;
    if(k == costsSize){
        for(int i = 0; i < costsSize; i++){
            ans = ans + costs[i] ;
        }
        return ans ;
    }
    
    bool* used = calloc( n, sizeof(bool) ) ;
    node** left = malloc(left_cn * sizeof(node*) ) ;
    node** right = malloc(right_cn * sizeof(node*) ) ;
    for(int i = 0; i < left_cn; i++){
        left[i] = malloc(sizeof(node) ) ;
        left[i]->val = costs[i] ;
        left[i]->idx = i ;
        used[i] = true ;
    }
    for(int i = 0; i < right_cn; i++){
        right[i] = malloc(sizeof(node) ) ;
        right[i]->val = costs[n-1-i] ;
        right[i]->idx = n-1-i ;
        used[n-1-i] = true ;
    }
    qsort(left, left_cn, sizeof(node*), cmp) ;
    qsort(right, right_cn, sizeof(node*), cmp) ;
    int l_idx = left_cn ;
    int r_idx = n-1-right_cn ;

    int item = 0 ;
    while(item < k){
        if(left_cn == 0){
            ans += heapPop(right, &right_cn) ;
            item++ ;
            continue ;
        }
        if(right_cn == 0){
            ans += heapPop(left, &left_cn) ;
            item++ ;
            continue ;
        }
        if(left[0]->val == right[0]->val && left[0]->idx == right[0]->idx){
            ans += left[0]->val ;
            heapPop(left, &left_cn) ;
            heapPop(right, &right_cn) ;
        }
        else if(left[0]->val <= right[0]->val){
            ans += left[0]->val ;
            if( used[l_idx] )
                heapPop(left, &left_cn) ;
            else{
                left[0]->val = costs[l_idx] ;
                left[0]->idx = l_idx ;
                used[l_idx] = true ;
                l_idx++ ;
                modifyHeap(left, left_cn) ;
            }
        }
        else{
            ans += right[0]->val ;
            if( used[r_idx] ){
                heapPop(right, &right_cn) ;
            }
            else{
                right[0]->val = costs[r_idx] ;
                right[0]->idx = r_idx ;
                used[r_idx] = true ;
                r_idx-- ;
                modifyHeap(right, right_cn) ;
            }
        }
        item++ ;
    }
    //free memory
    free(used) ;
    for(int i = 0; i < right_cn; i++)
        free(right[i]) ;
    for(int i = 0; i < left_cn; i++)
        free(left[i]) ;
    free(left) ;
    free(right) ;
    return ans ;
}