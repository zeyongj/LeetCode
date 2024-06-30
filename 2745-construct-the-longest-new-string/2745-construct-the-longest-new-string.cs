public class Solution {
    public int LongestString(int x, int y, int z) {
        int ans = 0;
        if (x == y)
            ans = 2 * Math.Min(x,y);
        else
            ans = 2 * Math.Min(x,y) + 1;
            
        ans += z;

        return ans * 2;        
    }
}