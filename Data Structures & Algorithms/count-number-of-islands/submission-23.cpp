class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count{0};
        vector<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        set<pair<int, int>> visited;
        queue<pair<int, int>> q;
        for (int i{0}; i < grid.size(); i++) {
            for (int j{0}; j < grid[0].size(); j++) {
                if (visited.contains({i, j}) || grid[i][j] == '0') continue; 
                
                q.push({i,j});
                count++;
                cout << grid[i][j] << endl;
                
                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop();
                    for (const auto& [dr, dc] : moves) {
                        int nr{r + dr}, nc{c + dc};
                        if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[0].size() && !visited.contains({nr, nc})) {
                            visited.insert({nr, nc});
                            if (grid[nr][nc] == '1') q.push({nr, nc});
                        }
                    }
                }
            }
        }
        return count;
    }
};
