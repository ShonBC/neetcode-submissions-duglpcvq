class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        // Time Complexity: O((rows*cols)log(rows*cols) Space Complexity: O(rows*cols))
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
        minHeap.push({0,0,0});
        int rows{int(heights.size()) - 1}, cols{int(heights[0].size()) - 1};
        while (!minHeap.empty()) {
            auto [e, r, c] = minHeap.top();
            minHeap.pop();
            if (visited.contains({r, c})) continue;
            visited.insert({r, c});
            if (r == rows && c == cols) return e;
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                if (min(nr, nc) >= 0 && nr < heights.size() && nc < heights[nr].size()) {
                    minHeap.push({max(e, abs(heights[r][c] - heights[nr][nc])), nr, nc});
                }
            }
        }
    }
};