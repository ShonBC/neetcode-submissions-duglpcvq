class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        /*
        visited set
        moves set
        deque for BFS
        count = 0
        itterate through grid, when a '1' is found -> increment count start BFS to define size of island by adding to visited set.
        BFS: if the explored node is in bounds, not in visited -> add to visited. 
             if node == '1' add to q 
        Time Complexity: O(row * col) Space Complexity: O(row * col)
        */

        set<pair<int, int>> visited; // {{row, col}}
        set<pair<int, int>> moves{{0,1}, {1,0}, {0,-1}, {-1,0}};
        deque<pair<int, int>> q; // {{row, col}}
        int count{0};
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (visited.contains({i, j}) || grid[i][j] != '1') continue;
                q.push_back({i,j});
                count++;
                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop_front();
                    for (auto [dr, dc] : moves) {
                        int nr{r + dr}, nc{c + dc};
                        if (min(nr, nc) >= 0 && nr < grid.size() && nc < grid[nr].size() && !visited.contains({nr, nc})) {
                            visited.insert({nr, nc});
                            if (grid[nr][nc] == '1') {
                                q.push_back({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
};
