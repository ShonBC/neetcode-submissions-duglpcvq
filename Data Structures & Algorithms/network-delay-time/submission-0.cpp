class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // times = {ui, vi, ti}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        heap.push({0, k}); // {time, n}
        int dist{0};
        set<int> visited;
        unordered_map<int, vector<pair<int, int>>> edges;
        for (const auto& t : times) {
            // construct adjacency list
            edges[t[0]].emplace_back(t[1], t[2]);
        }

        while (!heap.empty()) {
            auto cur = heap.top();
            heap.pop();
            int t1 = cur.first, n1 = cur.second;

            if (visited.contains(n1)) continue;
            visited.insert(n1);
            dist = t1;
            for (auto [n2, t2] : edges[n1]) {
                if (!visited.contains(n2)) {
                    heap.push({t1 + t2, n2});
                }
            }
        }
        return visited.size() == n ? dist : -1;
    }
};
