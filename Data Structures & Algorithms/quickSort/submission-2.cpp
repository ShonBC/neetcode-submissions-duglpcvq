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
    void split(vector<Pair>& pairs, int s, int e) {
        if (s >= e) {
            return;
        }
        Pair pivot = pairs[e];
        int left = s; 
        for (int i = s; i < e; i++) {
            if (pairs[i].key < pivot.key) {
                swap(pairs[i], pairs[left]);
                left++;
            }
        }
        swap(pairs[left], pairs[e]);
        split(pairs, s, left - 1);
        split(pairs, left + 1, e);
    }

    vector<Pair> quickSort(vector<Pair>& pairs) {
        split(pairs, 0, pairs.size() - 1);
        return pairs;
    }
};
