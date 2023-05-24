#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int jump(int* nums, int numsSize){
        int dp[numsSize];
        for(int i = 0; i < numsSize; i++) {
            dp[i] = INT_MAX;
        }
        dp[numsSize-1] = 0;
        for(int i=numsSize-2; i>=0; i--) {
            int steps = fmin(numsSize-1, i + nums[i]);
            for(int j=i+1; j<=steps; j++) {
                if(dp[j] != INT_MAX) {
                    dp[i] = fmin(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[0];
}