class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        // Time Complexity: O((rows*cols)log(rows*cols) Space Complexity: O(rows*cols))
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> minHeap;
        minHeap.push({0, {0,0}});
        int rows = int(heights.size()) - 1, cols{int(heights[0].size()) - 1};
        while (!minHeap.empty()) {
            auto [cost, node] = minHeap.top();
            int r{node.first}, c{node.second};
            minHeap.pop();
            if (visited.contains({r, c})) continue;
            visited.insert({r,c});
            if (r == rows && c == cols) return cost;
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                if (min(nr, nc) >= 0 && nr < rows + 1 && nc < cols + 1 && !visited.contains({nr, nc})){
                    int ncost = max(cost, abs(heights[r][c] - heights[nr][nc]));
                    minHeap.push({ncost, {nr, nc}});
                }
            }
        }
    }
};