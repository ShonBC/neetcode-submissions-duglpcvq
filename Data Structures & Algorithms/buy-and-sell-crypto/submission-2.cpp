class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof{0};
        int low{prices[0]};
        for (int cur : prices) {
            if (cur - low > prof) prof = cur - low;
            if (cur < low) low = cur;
        }
        return prof;
    }
};
