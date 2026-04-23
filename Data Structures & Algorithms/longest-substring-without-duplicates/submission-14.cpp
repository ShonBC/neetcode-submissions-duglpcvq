class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l{0}, ans{0};
        unordered_set<char> seen;
        for (char c : s) {
            while (seen.contains(c)) {
                seen.erase(s[l]);
                l++; 
            }
            seen.insert(c);
            ans = max(ans, int(seen.size()));
        }
        return ans;
    }
};
