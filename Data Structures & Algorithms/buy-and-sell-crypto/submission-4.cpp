class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof{0}, buy{prices[0]};
        for (int stock : prices) {
            int cur{stock - buy};
            prof = max(prof, cur);
            buy = min(buy, stock);
        }
        return prof;
    }
};
