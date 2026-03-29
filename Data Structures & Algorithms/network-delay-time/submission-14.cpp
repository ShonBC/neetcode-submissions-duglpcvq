class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Time Complexity: O(ElogE) maintinaing min heap of size edges
        // Space Complexity: O(V + E)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        unordered_map<int, vector<pair<int, int>>> edges;
        set<int> visited;
        int total{0};
        for (auto t : times) {
            edges[t[0]].push_back({t[2], t[1]});
        }
        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [t1, v1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(v1)) continue;
            visited.insert(v1);
            total = t1;
            for (auto [t2, v2] : edges[v1]) {
                if (!visited.contains(v2)) {
                    minHeap.push({t1 + t2, v2});
                }
            }
        }
        return visited.size() == n ? total : -1;
    }
};
