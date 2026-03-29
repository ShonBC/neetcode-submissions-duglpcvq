class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int r = 1;
        int l = 1;

        while (r < nums.size()) {
            if (nums[r] != nums[r - 1]) {
                nums[l] = nums[r];
                l++; 
            }
            r++;
        }
        return l;
    }
};