class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Time Complexity O(V * E) Space Complexity: O(V + E)
        unordered_map<int, vector<pair<int, int>>> edges; // {node : [cost, dst]}
        vector<int> prices(n, INT_MAX);
        deque<tuple<int, int, int>> q;
        q.push_back({0, src, 0}); // cost, node, num stops
        for (auto f : flights) {
            edges[f[0]].push_back({f[2], f[1]});
        }
        while (!q.empty()) {
            auto [c1, o1, s1] = q.front();
            q.pop_front();
            if (s1 > k) continue;
            for (auto [c2, o2] : edges[o1]) {
                int ncost{c1 + c2};
                if (ncost < prices[o2]) {
                    prices[o2] = ncost;
                    q.push_back({ncost, o2, s1 + 1});
                }
            }
        }
        return prices[dst] != INT_MAX ? prices[dst] : -1;
    }
};
