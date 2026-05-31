class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        array<int, 27> check1{0};
        for (char c : s1) {
            int cur = c - 'a';
            check1[cur]++;
        }
        array<int, 27> check2{0};
        int l{0}, r{0};
        while (r < s2.size()) {
            check2[s2[r] - (int)'a']++;
            if (check1 == check2) return true;

            r++;
            if (r - l == s1.size()) {
                check2[s2[l] - (int)'a']--;
                l++;
            }
        }
        return false;
    }
};
