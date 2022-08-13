class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        
        unordered_map<string, int> M, temp;
        vector<int> Ans;
        int N = words.size();
        int L = words[0].size();

        for(auto &it : words) {
            M[it]++;
        }
        int size = s.length();

        for(int i = 0; i < size - N*L + 1; i++) {
            
  
            for(int j = i; j < i + N*L; j+= L) {
                string ans = s.substr(j, L);
                temp[ans]++;
            }
            
            int flag = 1;
            

            for(auto &it : M) {
                if(M[it.first] != temp[it.first]) {
                    flag = 0;
                    break;
                }
            }
 
            if(flag) Ans.push_back(i);
            
            temp.clear();
        }
        
        return Ans;
    }
};