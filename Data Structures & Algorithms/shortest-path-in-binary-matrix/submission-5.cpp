class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1}, {1,0}, {0,-1}, {-1,0}, 
                                            {1,1}, {-1,-1}, {1,-1}, {-1,1}};
        deque<pair<int, int>> q;
        int steps{1};
        int rows = grid.size() - 1;
        int cols = grid[rows].size() - 1;
        if (grid[0][0] == 1 || grid[rows][cols] == 1) return -1;
        q.push_back({0,0});
        while (!q.empty()) {
            int layer = q.size();
            for (int i = 0; i < layer; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                if (r == rows && c == cols) return steps;
                for (auto [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] != 1) q.push_back({nr, nc});
                    }
                }
            }
            steps++;
        }
        return -1;
    }
};