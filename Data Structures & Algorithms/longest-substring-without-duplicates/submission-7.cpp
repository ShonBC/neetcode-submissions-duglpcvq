class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans{0};
        int left{0};
        set<char> chars;
        for (int i = 0; i < s.size(); i++) {
            while (chars.find(s[i]) != chars.end()) {
                chars.erase(s[left]);
                left++;
            }
            chars.insert(s[i]);
            ans = max(ans, i - left + 1);
        }
        return ans;
    }
};
