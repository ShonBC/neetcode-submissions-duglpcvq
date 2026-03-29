class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Time: O(V * E) Space: O(V + E)
        vector<int> prices(n, INT_MAX); // prices[i] = cost to destination[i]
        unordered_map<int, vector<pair<int, int>>> edges; // {origin : [dest, cost]}
        for (auto f : flights) {
            int ori = f[0], dst1 = f[1], cst = f[2];
            edges[ori].push_back({dst1, cst});
        }

        deque<tuple<int, int, int>> q; // [cst, ori, stops]
        q.push_back({0, src, 0});
        while (!q.empty()) {
            auto [cst, ori, stp] = q.front();
            q.pop_front();
            if (prices[ori] > cst) prices[ori] = cst;
            if (stp > k) continue;
            for (auto [dst1, cst2] : edges[ori]) {
                q.push_back({cst + cst2, dst1, stp + 1});
            }
        }
        return prices[dst] != INT_MAX ? prices[dst] : -1;
    }
};
