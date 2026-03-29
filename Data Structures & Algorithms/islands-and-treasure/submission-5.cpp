class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        set<pair<int, int>> visited;
        deque<pair<int, int>> q;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (!visited.contains({i, j}) && grid[i][j] == 0) {
                    q.push_back({i, j});
                    visited.insert({i,j});
                }
            }
        }

        int dist{0};
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        while (!q.empty()) {
            
            auto layer = q.size();
            for (int i = 0; i < layer; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                if (grid[r][c] == 2147483647) grid[r][c] = dist;
                for (auto [dr, dc] : moves) {
                    int nr = r + dr;
                    int nc = c + dc;
                    if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
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
