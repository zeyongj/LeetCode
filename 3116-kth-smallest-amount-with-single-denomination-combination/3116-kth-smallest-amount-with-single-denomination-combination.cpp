class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
     
      using ll = long long;
      int n = coins.size();
      vector<ll> mult(1 << n, 1);
      for (int b = 0; b < (1 << n); ++b) {
        for (int i = 0; i < n; ++i) {
          if (b & (1 << i)) {
            mult[b] = mult[b] / gcd(mult[b], coins[i]) * coins[i];
          }
        }
      }
      ll lo = 1, hi = 1e12;
      while (lo < hi) {
        ll mid = (lo + hi) / 2;
        ll cnt = 0;
        for (int b = 1; b < (1 << n); ++b) {
          ll v = mid / mult[b];
          if (__builtin_popcount(b) & 1) cnt += v;
          else cnt -= v;
        }
        if (cnt < k) lo = mid + 1;
        else hi = mid;
      }
      return lo;
        
    }
};