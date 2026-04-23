class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> seen;
        int maxf{0}, l{0}, ans{0};
        for (int r{0}; r < s.size(); r++) {
            seen[s[r]]++;
            maxf = max(seen[s[r]], maxf);
            while (r - l + 1 - maxf > k) {
                seen[s[l]]--;;
                l++;
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};
