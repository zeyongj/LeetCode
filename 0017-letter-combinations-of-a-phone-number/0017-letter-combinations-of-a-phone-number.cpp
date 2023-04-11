#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        unordered_map<char, string> phone{
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
        };
        
        vector<string> result;
        backtrack("", digits, 0, phone, result);
        return result;
    }
    
    void backtrack(string combination, string digits, int index, unordered_map<char, string> &phone, vector<string> &result) {
        if (index == digits.size()) {
            result.push_back(combination);
            return;
        }
        
        string letters = phone[digits[index]];
        for (const char &letter : letters) {
            combination.push_back(letter);
            backtrack(combination, digits, index + 1, phone, result);
            combination.pop_back();
        }
    }
};
