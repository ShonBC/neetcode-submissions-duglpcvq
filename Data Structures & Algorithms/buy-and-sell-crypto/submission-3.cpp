class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof{0};
        int low{prices[0]};
        for (int cur : prices) {
            prof = max(prof, cur - low);
            low = min(low, cur);
        }
        return prof;
    }
};
