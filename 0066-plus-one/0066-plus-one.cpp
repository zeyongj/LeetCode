class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int idx = n - 1; idx >= 0; idx--) {
          if (digits[idx] == 9)
            digits[idx] = 0;
          else {
            digits[idx]++;
            return digits;
          }
        }
        digits = vector<int>(++n);
        digits[0] = 1;
        return digits;
    }
};