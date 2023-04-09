class Solution {
    public boolean isUgly(int n) {
       if (n <= 0)
            return false;
        
        for (; n % 3 == 0 ; n /= 3);
        for (; n % 5 == 0 ; n /= 5);
        
        return (n & (n - 1)) == 0;
    }
}