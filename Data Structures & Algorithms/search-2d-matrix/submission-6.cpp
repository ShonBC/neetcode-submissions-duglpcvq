class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0;
        int bot = matrix.size() - 1;
        int col = 0;
        int mid_row;
        
        while (top <= bot) {
            mid_row = round((bot + top) / 2);
            if (target > matrix[mid_row].back()) {
                top = mid_row + 1;                
            }
            else if (target < matrix[mid_row][col]) {
                bot = mid_row - 1;
            }
            else break;
            
        }

        if (top > bot) return false;
        int left = 0;
        int right = matrix[0].size() - 1;

        while (left <= right) {
            int mid_col = round((left + right) / 2);
            int val = matrix[mid_row][mid_col]; 
            if (target > val) {
                left = mid_col + 1;
            }
            else if (target < val) {
                right = mid_col - 1;
            }
            else return true;
            
        }
        return false;
    }
};
