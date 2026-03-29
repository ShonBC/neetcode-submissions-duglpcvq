class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // Time and Space Complexity: O(row * col)
        int fresh{0};
        int time{0};
        set<pair<int, int>> visited;
        deque<pair<int, int>> q;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        for (int i = 0; i< grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 1) fresh++;
                else if (grid[i][j] == 2) q.push_back({i,j});
            }
        }
        while (!q.empty() and fresh) {
            int layer = q.size();
            for (int i = 0; i < layer; i++){
                auto [r, c] = q.front();
                q.pop_front();
                for (auto [dr, dc] : moves) {
                    int nr{r + dr}, nc{c + dc};
                    if (min(nr, nc) >= 0 && nr < grid.size() and nc < grid[nr].size() and !visited.contains({nr, nc})) {
                        visited.insert({nr, nc});
                        if (grid[nr][nc] == 1) {
                            grid[nr][nc] = 2;
                            fresh--;
                            q.push_back({nr, nc});
                        }
                    }
                }
            }
            time++;       
        }
        return !fresh ? time : -1;
    }
};
