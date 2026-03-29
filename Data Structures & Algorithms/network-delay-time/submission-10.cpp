class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        /*
        visited set {vi}
        adj list edges = {ui : [[ti, vi]]}
        minHeap {{cost, ui}}
        time{0}

        First create adj list using times and edges

        add {cost = 0, k} to minHeap
        Dijkstra:
        while minHeap is not empty -> pop from heap
        if node is in visited -> skip it
        Otherwise add to visited and set time = cost to get to node
        explore edges associated with node.
        for each edge -> if edge not in visited -> push to minHeap with {cost of first node + cost of new node, new node}
        
        return time if visited.size() == n else -1

        Time Complexity: O(Elog(E)) maintian a heap of size = # of edges 
        Space Complexity: O(V + E) visited is size = # of nodes and minHeap is size of number of edges
        */
        unordered_set<int> visited; // {vi}
        unordered_map<int, vector<pair<int, int>>> edges; // {ui : [[ti, vi]]}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap; // {{cost, ui}}
        int time{0};

        for (auto t : times) {
            edges[t[0]].push_back({t[2], t[1]});
        }

        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto [c1, v1] = minHeap.top();
            minHeap.pop();
            if (visited.contains(v1)) continue;
            visited.insert(v1);
            time = c1;
            for (auto [c2, v2] : edges[v1]) {
                if (!visited.contains(v2)) {
                    minHeap.push({c1 + c2, v2});
                }
            }
        }
        return visited.size() == n ? time : -1;
    }
};
