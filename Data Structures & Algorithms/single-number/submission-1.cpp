class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> visited;
        for (const int& n : nums) {
            if (visited.contains(n)) {
                visited[n]++;
            }
            else visited[n] = 1;
        }
        for (const auto& entry : visited) {
            if (entry.second == 1) return entry.first;
        }
    }
};
