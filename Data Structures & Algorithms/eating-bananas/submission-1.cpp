class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
    int l = 1;
    int r = *std::max_element(piles.begin(), piles.end());
    int ans = r;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        int time = 0;

        for (int p : piles) {
            time += ceil((double)p / mid);
            }
        if (time <= h) {
            ans = mid;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    return ans;
    }
};
