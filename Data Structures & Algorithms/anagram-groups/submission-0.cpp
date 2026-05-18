class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> table;
        for (string s: strs) {
            string current = s;
            sort(current.begin(), current.end());
            table[current].push_back(s);
        }
        vector<vector<string>> result;
        for (auto [key, val] : table) {
            result.push_back(val);
        }
    return result;
    }
    
};
