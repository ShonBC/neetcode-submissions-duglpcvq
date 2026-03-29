class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Time: O((V + E)log(v) Space: O(V + E)
        set<int> visited;
        priority_queue<pair<int , int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // {t, n}
        unordered_map<int, vector<pair<int, int>>> edges; // {n : [v, t]}
        for (auto node : times) {
            int n = node[0];
            int v = node[1];
            int t = node[2];
            edges[n].push_back({v, t});
        }

        int total{0};
        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [t1, n1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(n1)) continue;
            visited.insert(n1);
            total = t1;
            for (auto [n2, t2] : edges[n1]) {
                if (!visited.contains(n2)) {
                    minHeap.push({t2 + total, n2});
                }
            }
        }
        return visited.size() == n ? total: -1;
    }
};
