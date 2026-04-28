class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l{0}, r{int(nums.size() - 1)};
        for (int i{0}; i < nums.size(); i++) {
            int mid{(r + l) / 2};
            int cur{nums[mid]};
            if (cur > target) r = mid;
            else if (cur < target) l = mid + 1;
            else return mid;
        }
        return -1;
    }
};
