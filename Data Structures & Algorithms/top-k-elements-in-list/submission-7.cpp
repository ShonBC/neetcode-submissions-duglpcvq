class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int n : nums) {
            count[n] = 1 + count[n];
        }
        vector<vector<int>> freq(nums.size() + 1);
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> ans;
        for (int i = freq.size() - 1; i > 0; i--) {
            for (int n : freq[i]) {
                ans.push_back(n);
                if (ans.size() == k) return ans;
            }
        }
        return ans;
    }
};
