class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> comp;
        for (int i = 0; i < nums.size(); i ++) {
            int temp = target - nums[i];
            if (comp.contains(temp)) return {comp[temp], i};
            comp[nums[i]] = i;
        }
    }
};
