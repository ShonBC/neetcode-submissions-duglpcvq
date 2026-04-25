class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        /*
        itterate through nums
        push to heap
        while top of heap idx is outside of window -> pop
        push top of heap to ans vector

        Time Complexity: O(nlogn) Space Complexity: O(n)
        */
        vector<int> ans;
        priority_queue<pair<int, int>> maxHeap; // {val, idx}
        for (int i{0}; i < nums.size(); i++) {
            maxHeap.push({nums[i], i});
            while (maxHeap.top().second < i - k + 1) maxHeap.pop();
            if (i >= k - 1) ans.push_back(maxHeap.top().first);
        }
        return ans;
    }
};
