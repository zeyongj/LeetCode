#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> map;
        for (const std::string& str : strs) {
            std::string key = str;
            std::sort(key.begin(), key.end());
            map[key].push_back(str);
        }

        std::vector<std::vector<std::string>> result;
        for (auto it = map.begin(); it != map.end(); ++it) {
            result.push_back(it->second);
        }

        return result;
    }
};
