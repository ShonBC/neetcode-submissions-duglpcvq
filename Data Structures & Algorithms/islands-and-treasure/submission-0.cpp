class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        deque<pair<int, int>> q;
        set<pair<int, int>> visited;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0) {
                    q.push_back({i, j});
                    visited.insert({i, j});
                }
            }
        }
        int dist{0};
        set<pair<int, int>> moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty()) {
            auto len = q.size();
            for (int i = 0; i < len; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                if (grid[r][c] == 2147483647) grid[r][c] = dist;
                for (auto [dr, dc] : moves) {
                    int nr = r + dr;
                    int nc = c + dc;
                    if (nr >= 0 && nr < grid.size() && nc >=0 && nc < grid[0].size() && !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] != -1) {
                            q.push_back({nr, nc});
                        }
                    }
                }
            }
            dist++;
        }
    }
};
