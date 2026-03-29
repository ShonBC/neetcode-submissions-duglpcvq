class Solution {
public:
    bool isValid(string s) {
        std::stack<int> stack;
        std::unordered_map<char,char> check = {
            {')' , '('},
            {'}' , '{'},
            {']' , '['},
        };
        for (char i : s) {
            if (check.count(i)) {
                if (!stack.empty() && check[i] == stack.top()) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stack.push(i);
            }
        }
        if (stack.empty()) {
            return true;
        }
        else {
            return false;
        }
    }
};
