class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);
        for (const auto& course : prerequisites) {
            inDegree[course[1]]++;
            adj[course[0]].push_back(course[1]);
        }
        queue<int> q;
        for (int i{0}; i < numCourses; i++) {
            if (inDegree[i] == 0) q.push(i);
        }
        int count{0};
        vector<int> ans;
        while (!q.empty()) {
            int cur{q.front()};
            q.pop();
            ans.push_back(cur);
            count++;
            for (const int& nei : adj[cur]) {
                inDegree[nei]--;
                if (inDegree[nei] == 0) q.push(nei);
            }
        }
        cout << count << " " << numCourses << "\n";
        reverse(ans.begin(), ans.end());
        return count == numCourses ? ans : vector<int> {};
    }
};
