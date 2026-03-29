// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> ans;
        for (int i = 0; i < pairs.size(); i++){
            int j = i - 1;
            while (j >= 0 && pairs[j].key > pairs[j + 1].key) {
                Pair temp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = temp;
                j--;
            }
            ans.push_back(pairs);
        }
        return ans;
    }
};
