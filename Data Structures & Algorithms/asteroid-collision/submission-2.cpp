class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> ans;

        for (int& val : asteroids) {
            while (!ans.empty() && val < 0 && ans.back() > 0) {
                int diff = val + ans.back();
                if (diff > 0) {
                    val = 0;
                }
                else if (diff < 0) {
                    ans.pop_back();
                }
                else {
                    val = 0;
                    ans.pop_back();
                }
            }
            if (val) {
                ans.push_back(val);
            }
        }
        return ans;
    }
};