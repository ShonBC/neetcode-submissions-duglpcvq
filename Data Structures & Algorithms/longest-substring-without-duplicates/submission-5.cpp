class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int ans{0};
        int left{0};
        for (int i = 0; i < s.size(); i++) {
            while (seen.find(s[i]) != seen.end()) {
                seen.erase(s[left]);
                left++;
            }
            seen.insert(s[i]);
            ans = max(ans, i - left + 1);
        }
        return ans;
    }
};
