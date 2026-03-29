class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size();

        while (start <= end) {
            int mid_idx = round((end + start) / 2);
            if (target == nums[mid_idx]) {
                return mid_idx;
            }
            else if (target < nums[mid_idx]) {
                end = mid_idx - 1;
            }
            else {
                start = mid_idx + 1;
            }
        }
        return -1;

    }
};
