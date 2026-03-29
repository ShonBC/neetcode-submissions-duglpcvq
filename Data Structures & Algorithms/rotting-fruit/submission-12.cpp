class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // Time and Space Complexity: O(rows * cols)
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        deque<pair<int, int>> q;
        int fresh{0}, time{0};
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                int node{grid[i][j]};
                if (node == 1) fresh++;
                else if (node == 2) {
                    q.push_back({i,j});
                    visited.insert({i,j});
                }
            }
        }
        while (!q.empty() && fresh) {
            int layer{q.size()};
            for (int i = 0; i < layer; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                for (auto [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] == 1) {
                            q.push_back({nr, nc});
                            fresh--;
                        }
                    }
                }
            }
            time++;
        }
        return !fresh ? time : -1;
    }
};
