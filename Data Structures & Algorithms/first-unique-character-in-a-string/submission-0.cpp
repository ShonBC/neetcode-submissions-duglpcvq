class Solution {
public:
    int firstUniqChar(string s) {
        int ans{INT_MAX};
        unordered_map<char, pair<int, int>> letters; // {letter, {index, count}}
        for (int i{0}; i < s.size(); i++) {
            char c{s[i]};
            letters[c].second++;
            letters[c].first = i;
        }
        for (const auto key : letters) {
            if (key.second.second == 1) ans = min(ans, key.second.first);
        }
        return ans == INT_MAX ? -1 : ans;
    }
};