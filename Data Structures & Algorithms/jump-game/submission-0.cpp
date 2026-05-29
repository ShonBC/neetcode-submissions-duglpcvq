class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            cout << goal << " " << i << " " << nums[i] << endl;
            if (goal - (i + nums[i]) <= 0) {
                goal = i;
            }
        }
        return goal == 0 ? true: false;
    }
};
