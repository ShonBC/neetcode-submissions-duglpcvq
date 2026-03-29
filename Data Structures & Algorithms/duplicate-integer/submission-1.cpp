class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> count;

        for (int num : nums) {
            if (count.count(num)) {
                return true;
            }
            else {
                count[num] = 1;
            }
        }
        return false;
    }
};