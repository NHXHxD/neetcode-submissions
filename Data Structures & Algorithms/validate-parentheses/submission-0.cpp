class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> close = {
            {'}', '{'},
            {']', '['},
            {')', '('}
        };        
        stack<char> curr;
        for (char c: s) {
            if (close.find(c) != close.end()){
                if (curr.size() == 0) return false;

                if (curr.size() > 0 && close[c] == curr.top()) curr.pop();
                else return false;

            }
            else curr.push(c);
        }
        if (curr.size() > 0) return false;
        return true;
    }
};
