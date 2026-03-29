#include <array>

class Solution {
public:
    void sortColors(vector<int>& nums) {
        std::array<int, 3> count = {};
        for (int num : nums) {
            count[num] ++;
        }

        int i = 0;
        for (int c = 0; c < count.size(); c++) {
            for (int j = 0; j < count[c]; j++) {
                nums[i] = c;
                i++;
            }
        }
    }
};