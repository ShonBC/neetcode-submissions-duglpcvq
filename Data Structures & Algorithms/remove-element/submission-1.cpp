class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int r = 0;
        int l = 0;
        while (r < nums.size()) {
            if (nums[r] != val) {
                nums[l] = nums[r];
                l++;
            }
            r++;
        }
        return l;
    }
};