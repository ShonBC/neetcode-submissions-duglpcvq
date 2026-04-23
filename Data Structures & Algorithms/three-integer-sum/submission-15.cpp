class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for (int i{0}; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l{i + 1}, r{int(nums.size() - 1)};
            while (l < r) {
                int total{nums[i] + nums[l] + nums[r]};
                if (total > 0) r--;
                else if (total < 0) l++;
                else {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (r > l && nums[r] == nums[r - 1]) r--;
                    l++;
                    r--;
                }
                
            }
        }
        return ans;
    }
};
