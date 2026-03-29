class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        // Time and Space Complexity: O(rows * cols)
        set<pair<int, int>> visited;
        deque<pair<int, int>> q;
        int length{1};
        int rows{grid.size() - 1}, cols{grid[rows].size() - 1};
        q.push_back({0,0});
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};

        while (!q.empty()) {
            auto layer{q.size()};
            for (int i = 0; i < layer; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                if (r == rows and c == cols) return length;
                else if (grid[r][c] == 1) continue;
                for (auto [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 and nr < grid.size() and nc < grid[nr].size() and !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] == 0) q.push_back({nr, nc});
                    }
                }
            }
            length++;
        }
        return -1;
    }
};