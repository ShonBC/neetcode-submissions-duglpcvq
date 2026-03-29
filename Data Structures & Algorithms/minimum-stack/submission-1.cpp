#include <algorithm>
class MinStack {
    private:
        std::vector<int> stack;
    public:
    MinStack() {}
    
    void push(int val) {
        stack.push_back(val);
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
        
    }
    
    int getMin() {
        return *std::min_element(stack.begin(), stack.end());
    }
};
