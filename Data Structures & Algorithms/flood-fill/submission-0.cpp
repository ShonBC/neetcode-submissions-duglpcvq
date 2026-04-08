class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        // Time and Space Complexity: O(m X n)
        vector<vector<int>> ans{image};
        int ori{image[sr][sc]};
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        set<pair<int, int>> visited;
        queue<pair<int, int>> q;
        q.push({sr, sc});
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            if (visited.contains({r, c}) || image[r][c] != ori) continue;
            visited.insert({r, c});
            ans[r][c] = color;
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                if (min(nr, nc) >= 0 && nr < image.size() && nc < image[nr].size() && image[nr][nc] == ori) {
                    q.push({nr, nc});
                }
            }
        }
        return ans;
    }
};