class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n, 0);
        stack<pair<int, int>> stack; // {temp, idx}
        for (int i = 0; i < n; i++) {
            int cur = temperatures[i];
            while (!stack.empty() && cur > stack.top().first) {
                auto pair = stack.top();
                stack.pop();
                ans[pair.second] = i - pair.second;
            }
            stack.push({cur, i});
        }
        return ans;
    }
};
