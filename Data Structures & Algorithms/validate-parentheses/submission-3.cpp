class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> check = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        std::stack<char> stack;
        for (char i : s) { 
            if (check.count(i)) {
                if (stack.size() > 0 && check[i] == stack.top()) {
                    stack.pop();
                }
                else return false;
            }
            else {
                stack.push(i);
            }
        }
        return stack.empty();
    }
};
