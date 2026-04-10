class Solution {
public:
    void solve(vector<vector<char>>& board) {
        // Time and Space Compleixty: O(rows X cols)
        deque<pair<int, int>> bfs_q;
        deque<pair<int, int>> mod_q;
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == 'O' && !visited.contains({i,j})) {
                    bfs_q.push_back({i,j});
                    bool is_edge{false};
                    while (!bfs_q.empty()) {
                        auto [r, c] = bfs_q.front();
                        bfs_q.pop_front();
                        mod_q.push_back({r,c});
                        visited.insert({r, c});
                        for (auto [dr, dc] : moves) {
                            int nr{r + dr}, nc{c + dc};
                            if (min(nr, nc) >= 0 && nr < board.size() && nc < board[nr].size()) {
                                if (board[nr][nc] == 'O' && !visited.contains({nr,nc})) {
                                    bfs_q.push_back({nr, nc});
                                }
                            }
                            else {
                                is_edge = true;
                            }
                        }
                    }
                    if (!is_edge) {
                        while (!mod_q.empty()) {
                            auto [r, c] = mod_q.front();
                            mod_q.pop_front();
                            board[r][c] = 'X';
                        }
                    }
                    else {
                        mod_q.clear();
                    }
                }
            }
        } 
    }
};
