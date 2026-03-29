class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> seen;
        int ans{0};
        int l{0};
        for (int i = 0; i < s.size(); i++) {
            while (seen.contains(s[i])) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[i]);
            ans = max(ans, i - l + 1);
        }
        return ans;
    }
};
