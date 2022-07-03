class Solution {
public:
  double myPow(double x, int n) {
    return n >= 0 ? myPowImp(x, n) : 1.0 / myPowImp(x, n);
  }
private:
  double myPowImp(double x, int n) {
    if (n == 0) return 1;
    return myPowImp(x * x, n / 2) * (n % 2 ? x : 1);
  }
};