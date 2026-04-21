class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Time Complexity: O(n) Space Complexity: O(n)
        unordered_set<char> seen;
        int ans{0};
        int idx{0};
        for (char c : s) {
            while (seen.contains(c)) {
                seen.erase(s[idx]);
                idx++;
            }
            seen.insert(c);
            ans = max(ans, int(seen.size()));
        }
        return ans;
    }
};
