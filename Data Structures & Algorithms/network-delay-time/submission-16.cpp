class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Time Complexity: O(ElogE) Space Complexity: O(V + E)
        set<int> visited;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        unordered_map<int, vector<pair<int, int>>> edges;
        int cost{0};
        for (auto t : times) {
            edges[t[0]].push_back({t[2], t[1]});
        }
        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [c1, v1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(v1)) continue;
            visited.insert(v1);
            cost = c1;
            for (auto [c2, v2] : edges[v1]) {
                int nc{c1 + c2};
                if (!visited.contains(v2)) minHeap.push({nc, v2});
            }
        }
        return visited.size() == n ? cost : -1;
    }
};
