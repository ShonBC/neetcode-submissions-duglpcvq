class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        // Time and Space Complexity: O(rows * cols)
        deque<vector<int>> q;
        set<pair<int, int>> visited;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        q.push_back(start);
        visited.insert({start[0], start[1]});
        while(!q.empty()) {
            vector<int> node = q.front();
            int r{node[0]}, c{node[1]};
            q.pop_front();
            if (r == destination[0] and c == destination[1]) return true;
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                while (min(nr, nc) >= 0 && nr < maze.size() && nc < maze[0].size() && maze[nr][nc] != 1){
                    nr += dr;
                    nc += dc;
                }
                nr -= dr;
                nc -= dc;
                if (!visited.contains({nr, nc})) {
                    visited.insert({nr, nc});
                    q.push_back({nr, nc});
                }
            }
        }
        return false;
    }
};
