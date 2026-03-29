class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int total{0};
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        set<int> visited;
        unordered_map<int, vector<pair<int, int>>> edges;
        for (auto t : times) {
            edges[t[0]].push_back({t[2], t[1]});
        }

        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [t1, u1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(u1)) continue;
            total = t1;
            visited.insert(u1);
            for (auto [t2, u2] : edges[u1]) {
                if (!visited.contains(u2)) {
                    minHeap.push({t1 + t2, u2});
                }
            }
        }
        return visited.size() == n ? total : -1;
    }
};
