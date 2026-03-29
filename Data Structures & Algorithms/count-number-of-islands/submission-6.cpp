class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        /*
        Traverse grid until a "1" is found. 
        use bfs to find all "1" and mark all nodes explored as seen.
        whenever the first "1" is found incrament the number of islands.
        */

        int ans{0};
        deque<pair<int, int>> q;
        set<pair<int, int>> seen;
        set<pair<int, int>> moves{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (!seen.contains({i, j}) && grid[i][j] == '1') {
                    ans++;
                    seen.insert({i, j});
                    q.push_back({i, j});
                    while (!q.empty()) {
                        auto [r, c] = q.front();
                        q.pop_front();
                        for (auto [dr, dc] : moves) {
                            int nr = r + dr;
                            int nc = c + dc;
                            if (!seen.contains({nr, nc}) && nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size()) {
                                seen.insert({nr, nc});
                                if (grid[nr][nc] == '1') {
                                    q.push_back({nr, nc});
                                }
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
