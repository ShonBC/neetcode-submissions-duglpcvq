class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        unordered_map<int, int> count;
        for (int val : nums) {
            count[val]++;
        }
        
        for (auto [val, c] : count) {
            heap.push({c, val});
            if (heap.size() > k) {
                heap.pop();
            }
        }
        vector<int> ans;
        while (!heap.empty()) {
            auto [c, val] = heap.top();
            heap.pop();
            ans.push_back(val);
        }
        return ans;
    }
};
