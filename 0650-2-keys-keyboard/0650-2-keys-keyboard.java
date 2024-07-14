class Solution {
    public int minSteps(int n) {
        if(n==1) return 0;
        if(n<=5) return n;
        return recur(n,1,1);
    }
    public int recur(int n, int curr_len, int copy_len){
        if(curr_len==n) return 1;
        if(curr_len>n) return 1001;
        int cpy_n_paste = 1001;
        if(copy_len != curr_len){
            cpy_n_paste = 2 + recur(n,curr_len*2,curr_len);
        }
        int paste = 1 + recur(n,curr_len+copy_len,copy_len);
        return Math.min(cpy_n_paste, paste);
    }
}