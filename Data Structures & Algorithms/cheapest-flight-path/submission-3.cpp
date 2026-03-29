class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> prices(n, INT_MAX); // prices[i] = cost to get to destination[i]
        unordered_map<int, vector<pair<int, int>>> edges; // {ori: [dst, cost]}
        for (auto f : flights) {
            edges[f[0]].push_back({f[1], f[2]});
        }
        deque<tuple<int, int, int>> q; // cost, ori, stops
        q.push_back({0, src, 0});
        while (!q.empty()) {
            auto [c1, o1, s1] = q.front();
            q.pop_front();
            if (s1 > k) continue;
            for (auto [o2, c2] : edges[o1]) {
                int ncost = c1 + c2;
                if (ncost < prices[o2]) {
                    prices[o2] = ncost;
                    q.push_back({ncost, o2, s1 + 1});
                }
            }
        }
        return prices[dst] != INT_MAX ? prices[dst] : -1;
    }
};
