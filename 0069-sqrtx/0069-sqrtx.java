import static java.lang.Math.*;
class Solution {
    public int mySqrt(int x) {
       if (x <= 1) 
           return x;
        for (long s = 1; s <= x; ++s){
          if (s * s > x) 
              return (int)s - 1;
        }
        return -1;
    }
}