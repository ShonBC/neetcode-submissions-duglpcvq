class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps{0}, l{0}, r{0};

        while (r < nums.size() - 1) {
            int mdist{max(l + nums[l], r + nums[r])};
            l = r + 1;
            r = mdist;
            jumps++;
        }
        return jumps;
    }
};
