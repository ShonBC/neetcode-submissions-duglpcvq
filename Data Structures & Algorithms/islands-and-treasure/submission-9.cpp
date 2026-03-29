class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        /*
        visited set
        move set
        dist
        q for multi-source BFS
        traverse grid and add all treasure to q
        perform BFS layer by layer until q is empty
        each layer: 
        pop form q -> if node is -1 then skip
        Otherwise add to visited -> grid[node] = dist -> explore surrounding nodes
        if new node is in bounds, not been visited -> add to visited
        if new node != -1 -> add to q

        After each layer increment distance 
        Time Complexity: O(row * col) Space Complexity: O(row * col)
        */

        set<pair<int, int>> visited; // {{row, col}}
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        int dist{0};
        deque<pair<int, int>> q; //{{row, col}}
        for (int i = 0; i < grid.size(); i ++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 0) q.push_back({i,j});
            }
        }

        while (!q.empty()) {
            int layer = q.size();
            for (int i = 0; i < layer; i++) {
                auto [r, c] = q.front();
                q.pop_front();
                if (grid[r][c] == -1) continue;
                visited.insert({r, c});
                grid[r][c] = dist;
                for (auto [dr, dc] : moves) {
                    int nr{r+dr}, nc{c+dc};
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
