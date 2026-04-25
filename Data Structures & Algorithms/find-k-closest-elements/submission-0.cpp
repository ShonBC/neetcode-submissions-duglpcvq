class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // {dist, val}
        vector<int> ans;
        for (const int& val : arr) {
            int dist{abs(val - x)};
            minHeap.push({dist, val});
        }
        // {4, 2, 1, 2}
        for (int i{0}; i < k; i++) {
            ans.push_back(minHeap.top().second);
            minHeap.pop();
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};