class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Time: O(Elog(V)) Space: O(V + E)
        set<int> visited; // u
        unordered_map<int, vector<pair<int, int>>> edges; // {u : [[v, t]]}
        for (auto t : times) {
            edges[t[0]].push_back({t[1], t[2]});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // {t, u}
        minHeap.push({0, k});
        int total{0};
        while (!minHeap.empty()) {
            auto [t1, u1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(u1)) continue;
            visited.insert(u1);
            total = t1;
            for (auto [u2, t2] : edges[u1]) {
                if (!visited.contains(u2)) {
                    minHeap.push({t1 + t2, u2});
                }
            }
        }
        return visited.size() == n ? total : -1;
    }
};
