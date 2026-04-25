class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l{0}, r{int(nums.size())};
        while (l < r) {
            int mid{l + (r - l) / 2};
            if (nums[mid] >= target) {
                r = mid;
            }
            else if (nums[mid] < target) {
                l = mid + 1;
            }
        }
        return (l < nums.size() && nums[l] == target) ? l : -1;
    }
};
