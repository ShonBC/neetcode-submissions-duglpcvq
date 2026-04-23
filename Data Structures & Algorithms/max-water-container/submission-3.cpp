class Solution {
public:
    int maxArea(vector<int>& heights) {
        // Time Complexity: O(n) Space Complexity: O(1)
        int l{0}, r{int(heights.size() - 1)};
        int ans{0};
        while (l < r) {
            ans = max(ans,min(heights[l], heights[r]) * (r - l));
            if (heights[l] > heights[r]) r--;
            else l++;
        }
        return ans;
    }
};
