class Solution {
public:
    void reverseString(vector<char>& s) {
        stack<char> word;
        for (char c : s) word.push(c);
        int i{0};
        for (int i{0}; i < s.size(); i++) {
            s[i] = word.top();
            word.pop();
        }
    }
};