class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> score;
        for (string& op : operations) {
            if (op == "+") {
                int first = score.back();
                int second = *(score.rbegin() + 1);
                int total = first + second;
                score.push_back(total);
            }
            else if (op == "D") {
                score.push_back(score.back() * 2);
            }
            else if (op == "C") {
                score.pop_back();
            }
            else {
                score.push_back(stoi(op));
            }
        }
        int ans{0};
        for (int val : score) {
            ans += val;
        }
        return ans;
    }
};