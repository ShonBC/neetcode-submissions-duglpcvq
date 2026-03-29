class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res = {{}};
        for (int num : nums) {
            int res_size = res.size();
            for (int i = 0; i < res_size; i++) {
                vector<int> sub = res[i];
                sub.push_back(num);
                res.push_back(sub);
            }
        }
        return res;
    }
};
