class Solution {
public:
    bool isPalindrome(string s) {
        // Time Complexity: O(n) Space Complexity: O(1)
        int l{0};
        int r{int(s.size()) - 1};
        while (l < r) {
            while (!isalnum(s[l]) && l < r) l++;
            while (!isalnum(s[r]) && r > l) r--;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++;
            r--;
        }
        return true;
    }
};
