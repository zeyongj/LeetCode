class Solution {
public:
    long long waysToBuyPensPencils(int x, int a, int b) {
        long long int ans = 0;
        for(int i = 0; i <= x/a; i++){
            ans += (x-(a*i))/b+1;
        }
        return ans;
    }
};