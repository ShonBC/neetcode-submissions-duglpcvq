class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visited;
        while (n != 1) {
            if (visited.contains(n)) {
                return false;
            }
            visited.insert(n);
            n = sumSquares(n);
        }
        return true;
    }
    int sumSquares(int n) {
        int total{0};
        while (n) {
            total += pow(n % 10, 2);
            n = n / 10;
        }
        return total;
    }
};
