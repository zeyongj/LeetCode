class Solution {
public:
    pair<int,int> factors(int num){
        pair<int,int> p;
        for(int i=2;i<=num/2;i++){
            if(num%i==0){
                p=make_pair(i,num/i);
                break;
            }
        }
        return p;
    }
    bool isPrime(int N) {
        for (int i = 2; i <= sqrt(N); i++) {
            if (N % i == 0) {
                return false;
            }
        }
        return true;
    }
    int minSteps(int n) {
        if(n>1 && isPrime(n)) return n;
        vector<int> dp(n+4,-1);
        dp[1]=0;
        dp[2]=2;
        dp[3]=3;
        if(n<=3) return dp[n];
        
        for(int i=4;i<=n/2;i++){
            if(isPrime(i)){
                dp[i]=i;
                continue;
            } 
            pair<int,int> fact=factors(i);
            int first=fact.first;
            int second=fact.second;
            dp[i]=dp[first]+dp[second];
        }
        pair<int,int> fact=factors(n);
        int first=fact.first;
        int second=fact.second;
        return dp[n]=dp[first]+dp[second];
    }
};