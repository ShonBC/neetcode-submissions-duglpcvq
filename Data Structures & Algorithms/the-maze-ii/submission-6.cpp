class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        // Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap; // {num steps, r, c}
        set<tuple<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        set<pair<int, int>> visited;
        minHeap.push({0,start[0],start[1]});
        while (!minHeap.empty()) {
            auto [steps, r, c] = minHeap.top();
            minHeap.pop();
            if (visited.contains({r, c})) continue;
            visited.insert({r, c});
            if (r == destination[0] && c == destination[1]) return steps;
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                int cur{1};
                while (min(nr, nc) >= 0 && nr < maze.size() && nc < maze[nr].size() && maze[nr][nc] != 1) {
                    nr += dr;
                    nc += dc;
                    cur++;
                }
                nr -= dr;
                nc -= dc;
                cur--;
                if (!visited.contains({nr, nc})) {
                    minHeap.push({steps + cur, nr, nc});
                }
            }
        }
        return -1;
    }
};
