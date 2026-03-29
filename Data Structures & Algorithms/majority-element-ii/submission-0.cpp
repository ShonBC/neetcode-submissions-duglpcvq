class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std::map<int, int> seen;
        for (int num : nums){
            auto it = find(nums.begin(), nums.end(), num);
            if (it == nums.end()) {
                seen.insert({num, 1});
            }
            else {
                seen[num]++;
            }
        }
        int size = nums.size();
        std::vector<int> ans;
        for (auto [key, val] : seen) {
            if (val > size / 3) {
                ans.push_back(key);
            }
        }
        return ans;
    }
};