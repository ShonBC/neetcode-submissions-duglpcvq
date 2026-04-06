class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        // Time and Space Complexity: O(n X n)
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
        deque<pair<int, int>> q;
        q.push_back({0,0});
        visited.insert({0,0});
        int rows{int(grid.size()) - 1}, cols{int(grid.size()) - 1};
        int path{1};
        while (!q.empty()) {
            auto layers{q.size()};
            for (int i = 0; i < layers; i++) {
                const auto& [r, c] = q.front();
                if (r == rows && c == cols) return path;
                q.pop_front();
                if (grid[r][c] == 1) continue;
                for (const auto& [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] == 0) q.push_back({nr, nc});
                    }
                }
            }
            path++;
        }
        return -1;
    }
};