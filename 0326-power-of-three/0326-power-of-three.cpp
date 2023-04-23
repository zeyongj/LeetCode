#include <cmath> 
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n < 0)
            return false;
        double ans = log10(n) / log10(3);
        return fabs(ans - round(ans)) <= 1e-10; //fabs( )主要是求精度要求更高的double ，float 型的绝对值
    }
};