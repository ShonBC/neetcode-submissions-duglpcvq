class Solution {
public:
    string findShortestWay(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
        // Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        priority_queue<tuple<int, int, int, string>, vector<tuple<int, int, int, string>>, greater<tuple<int, int, int, string>>> minHeap; // {num steps, r, c, path}
        set<tuple<int, int, string>> moves{{0,1,"r"},{1,0,"d"},{0,-1,"l"},{-1,0,"u"}};
        set<pair<int, int>> visited;
        minHeap.push({0,ball[0],ball[1], ""});
        while (!minHeap.empty()) {
            auto [steps, r, c, path] = minHeap.top();
            minHeap.pop();
            if (visited.contains({r, c})) continue;
            visited.insert({r, c});
            if (r == hole[0] && c == hole[1]) return path;
            for (auto [dr, dc, p] : moves) {
                int nr{r + dr}, nc{c + dc};
                int cur{1};
                bool hit_hole{false};
                while (min(nr, nc) >= 0 && nr < maze.size() && nc < maze[nr].size() && maze[nr][nc] != 1) {
                    if (nr == hole[0] && nc == hole[1]) {
                        hit_hole = true;
                        break;
                    }
                    nr += dr;
                    nc += dc;
                    cur++;
                }
                if (!hit_hole) {
                    nr -= dr;
                    nc -= dc;
                    cur--;
                }
                if (!visited.contains({nr, nc})) {
                    minHeap.push({steps + cur, nr, nc, path + p});
                }
            }
        }
        return "impossible";
    }
};
