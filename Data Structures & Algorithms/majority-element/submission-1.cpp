class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans{nums[0]};
        int count{0};
        for (int val : nums) {
            if (val == ans) {
                count++;
            }
            else {
                count--;
                if (count <= 0) {
                    ans = val;
                    count = 1;
                }
            }
        }
        return ans;
    }
};