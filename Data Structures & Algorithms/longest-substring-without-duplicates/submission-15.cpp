class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left{0}, count{0};
        set<char> seen;
        for (const char c : s) {
            while (seen.contains(c)) seen.erase(s[left++]);
            seen.insert(c);
            count = max(count, static_cast<int>(seen.size()));
        }
        return count;
    }
};
