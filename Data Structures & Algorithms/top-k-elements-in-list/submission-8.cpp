class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (const int& val : nums) counts[val] = 1 + counts[val];
        
        vector<vector<int>> freq(nums.size() + 1);
        for (const auto& entry : counts) {
            int c{entry.second}, val{entry.first};
            freq[c].push_back(val);
        }
        vector<int> ans;
        for (int i = freq.size() - 1; i >= 0; i--) {
            for (const int& val : freq[i]) {
                ans.push_back(val);
                if (ans.size() == k) return ans;
            }
        }
        return ans;
    }
};
