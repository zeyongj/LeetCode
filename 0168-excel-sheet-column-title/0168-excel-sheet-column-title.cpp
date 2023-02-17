class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res;       
        
        while(columnNumber){
            columnNumber -= 1;
            char temp='A' + columnNumber%26;
            res = temp + res;
            columnNumber /= 26;
        }
       
    return res;    
    }
};