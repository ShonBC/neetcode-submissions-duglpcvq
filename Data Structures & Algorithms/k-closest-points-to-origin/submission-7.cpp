class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> max_heap;
        for (auto& p : points) {
            int x = p[0], y = p[1];
            int dist = pow(x, 2) + pow(y, 2);
            max_heap.push({dist, {x, y}});
            if (max_heap.size() > k) {
                max_heap.pop();

            }
        }

        vector<vector<int>> ans;
        while (!max_heap.empty()) {
            ans.push_back(max_heap.top().second);
            max_heap.pop();
        }
        return ans;
    }
};
