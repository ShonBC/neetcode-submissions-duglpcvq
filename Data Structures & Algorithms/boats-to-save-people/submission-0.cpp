class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int ans = 0;
        sort(people.begin(), people.end());
        int l = 0;
        int r = people.size() - 1;
        while (l <= r) {
            if (people[l] + people[r] > limit) {
                if (people[r] <= limit) {
                    ans++;
                }
                r--;
            }
            else {
                l++;
                r--;
                ans++;
            }
        }
        return ans;
    } // 1 2 2 3 3 
};