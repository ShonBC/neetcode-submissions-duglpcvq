class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans{0};
        int l{0};
        set<char> seen;
        for (int i = 0; i < s.size(); i++) {
            while (seen.contains(s[i])) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[i]);
            ans = max(ans, (int)seen.size());
        }
        return ans;
    }
};
