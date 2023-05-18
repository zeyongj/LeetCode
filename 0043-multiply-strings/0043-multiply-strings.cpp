#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        int n1 = num1.size();
        int n2 = num2.size();
        vector<int> result(n1 + n2, 0);

        for (int i = n1 - 1; i >= 0; --i) {
            for (int j = n2 - 1; j >= 0; --j) {
                int product = (num1[i] - '0') * (num2[j] - '0');
                int sum = product + result[i + j + 1];
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }

        // Convert the result to string
        string resultStr;
        for (int i = 0; i < result.size(); ++i) {
            if (!(resultStr.empty() && result[i] == 0)) // Skip leading zeros
                resultStr.push_back(result[i] + '0');
        }

        return resultStr.empty() ? "0" : resultStr;
    }
};
