class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        // Time and Space Complexity: O(rows * cols)
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
        deque<tuple<int, int, int>> q;
        q.push_back({0,0,1});
        visited.insert({0,0});
        int rows{int(grid.size()) - 1}, cols{int(grid[0].size()) - 1};
        while (!q.empty()) {
            auto layer{q.size()};
            for (int i = 0; i < layer; i++) {
                auto [r, c, l] = q.front();
                q.pop_front();
                if (grid[r][c] == 1) continue;
                else if (r == rows && c == cols) return l;
                for (auto [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] == 0) q.push_back({nr, nc, l + 1});
                    }
                }
            }
        }
        return -1;
    }
};