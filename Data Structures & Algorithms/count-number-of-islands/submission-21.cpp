class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // Time and Space Complexity: O(rows * cols)
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        int count{0};
        deque<pair<int, int>> q;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (visited.contains({i, j}) || grid[i][j] == '0') continue;
                q.push_back({i, j});
                count++;
                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop_front();
                    for (auto [dr, dc] : moves) {
                        int nr{r + dr}, nc{c + dc};
                        if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                            visited.insert({nr, nc});
                            if (grid[nr][nc] == '1') q.push_back({nr, nc});
                        }
                    }
                }
            }
        }
        return count;
    }
};
