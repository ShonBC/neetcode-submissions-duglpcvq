class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // sort -> difference of l and r pointer used to find third in vector O(n**2) time
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 and nums[i] == nums[i - 1]) continue;
            int l = i + 1, r{int(nums.size() - 1)};
            while (l < r) {
                int sum{nums[i] + nums[r] + nums[l]};
                if (sum == 0) {
                    ans.push_back({nums[l], nums[r], nums[i]});
                    while (r > l && nums[r] == nums[r - 1]) r--;
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    r--;
                    l++;
                }
                else if (sum > 0) r--;
                else l++;
            }
        }
        return ans;
    }
};
