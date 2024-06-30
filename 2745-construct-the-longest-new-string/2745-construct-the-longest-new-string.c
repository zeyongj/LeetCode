int longestString(int x, int y, int z){
    int ans = 0;
    if (x == y)
        ans = 2 * fmin(x,y);
    else
        ans = 2 * fmin(x,y) + 1;
            
    ans += z;

    return ans * 2;
}