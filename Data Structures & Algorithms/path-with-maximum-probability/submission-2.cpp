class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        // Time Complexity: O((E + V)log(V) Space Complexity: O(E + V) E = num edges V = num nodes 
        priority_queue<pair<double, int>> heap; // {prob, node}
        unordered_map<int, vector<pair<int, double>>> adj; // from : {{to, prob}}
        set<int> visited; // node
        for (int i = 0; i < edges.size(); i++) {
            vector<int>& cur{edges[i]};
            adj[cur[0]].push_back({cur[1], succProb[i]});
            adj[cur[1]].push_back({cur[0], succProb[i]});
        }
        heap.push({1, start_node});
        while (!heap.empty()) {
            auto [prob, node] = heap.top();
            heap.pop();
            cout << prob << " " << node << "\n";
            if (visited.contains(node)) continue;
            visited.insert(node);
            if (node == end_node) return prob;
            for (auto [to, p2] : adj[node]) {
                heap.push({prob * p2, to});
            }
        }
        return 0;
    }
};