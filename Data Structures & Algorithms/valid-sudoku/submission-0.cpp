class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        map<pair<int, int>, unordered_set<char>> boxes;

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                char c = board[i][j];
                if (c != '.') {
                    pair<int, int> box_index = {i/3, j/3};
                    if (rows[i].count(c) || cols[j].count(c) || boxes[box_index].count(c)) return false;
                    rows[i].insert(c);
                    cols[j].insert(c);
                    boxes[box_index].insert(c);
                }
            }
        }
        return true;
    }
};
