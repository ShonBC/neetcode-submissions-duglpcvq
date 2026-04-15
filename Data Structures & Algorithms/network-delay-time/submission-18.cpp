class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        set<int> visited;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // cost, to
        unordered_map<int, vector<pair<int, int>>> edges; // from : to, cost
        for (auto t : times) {
            int u{t[0]}, v{t[1]}, c{t[2]};
            edges[u].push_back({c, v});
        }

        int time{0};
        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [c, o] = minHeap.top();
            minHeap.pop();
            if (visited.contains(o)) continue;
            visited.insert(o);
            time = c;
            for (auto [c2, o2] : edges[o]) {
                int ncost{c + c2};
                minHeap.push({ncost, o2});
            }
        }
        return n == visited.size() ? time : -1;
    }
};
