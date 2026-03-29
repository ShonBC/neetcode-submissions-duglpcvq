class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans{0};
        set<pair<int, int>> visited;
        set<pair<int, int>> moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        deque<pair<int, int>> q;

        for (int i = 0; i < grid.size(); i ++) {
            for (int j = 0; j < grid[0].size(); j ++) {
                if (grid[i][j] == '1' && !visited.contains({i, j})) {
                    ans++;
                    q.push_back({i,j});
                    // Find island boundry
                    while (!q.empty()){
                        auto [r, c] = q.front();
                        q.pop_front();
                        for (auto [dr,dc] : moves) {
                            int newr = r + dr;
                            int newc = c + dc;
                            if (0 <= newr && newr < grid.size() && 0 <= newc && newc < grid[0].size() && !visited.contains({newr, newc})) {
                                visited.insert({newr, newc});
                                if (grid[newr][newc] == '1') q.push_back({newr, newc});
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
