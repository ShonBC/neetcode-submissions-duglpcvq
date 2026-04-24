class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // compare each letter of each word. if the letters dont match return the prefix 
        string prefix{""};
        for (int i{0}; i < strs[0].size(); i++) {
            char cur{strs[0][i]};
            for (string s : strs) {
                if (s[i] != cur) return prefix;
            }
            prefix += cur;
        }
        return prefix;
    }
};