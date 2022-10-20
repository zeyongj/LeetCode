class Solution {
public:
    string intToRoman(int num) {
        const int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};    
        const string symbols[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"}; 
        string s;
        for (int i = 0; i < 13; i++) {
            while (values[i] <= num) {
                num -= values[i];
                s.append(symbols[i]);
            }
        }
        return s;
    }
};