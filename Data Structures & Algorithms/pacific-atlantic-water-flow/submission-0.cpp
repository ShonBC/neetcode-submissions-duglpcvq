class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        queue<pair<int, int>> p_q;
        queue<pair<int, int>> a_q;
        set<pair<int, int>> p_set;
        set<pair<int, int>> a_set;
        set<pair<int, int>> moves{{0,1},{1,0},{0,-1},{-1,0}};
        // Build Queue's 
        for (int i = 0; i < heights.size(); i++) {
            for (int j = 0; j < heights[0].size(); j++) {
                if (i == 0 || j == 0) {
                    p_q.push({i,j});
                }
                if (i == heights.size() - 1 || j == heights[0].size() - 1) {
                    a_q.push({i,j});
                }
            }
        }
        
        while (!p_q.empty()) {
            auto [r, c] = p_q.front();
            p_q.pop();
            p_set.insert({r, c});
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                if (min(nr, nc) >= 0 && nr < heights.size() && nc < heights[0].size() && !p_set.contains({nr, nc}) && heights[nr][nc] >= heights[r][c]) {
                    p_q.push({nr, nc});
                    p_set.insert({nr, nc});
                }
            }
        }
        while (!a_q.empty()) {
            auto [r, c] = a_q.front();
            a_q.pop();
            a_set.insert({r, c});
            for (auto [dr, dc] : moves) {
                int nr{r + dr}, nc{c + dc};
                if (min(nr, nc) >= 0 && nr < heights.size() && nc < heights[0].size() && !a_set.contains({nr, nc}) && heights[nr][nc] >= heights[r][c]) {
                    a_q.push({nr, nc});
                    a_set.insert({nr, nc});
                }
            }
        }
        vector<vector<int>> ans;
        for (auto [r, c] : p_set) {
            if (a_set.contains({r,c})) ans.push_back({r, c});
        }
        return ans;
    }
};
