class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prev{prices[0]};
        int prof{0};
        for (int val : prices) {
            if (val > prev) {
                prof += val - prev;
            }
            prev = val;
        }
        return prof;
    }
};