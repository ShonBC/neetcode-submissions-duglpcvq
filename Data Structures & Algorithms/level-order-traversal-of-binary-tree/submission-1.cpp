/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <deque>

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::deque<TreeNode*> q;
        vector<vector<int>> ans;
        if (root) {
            q.push_back(root);
        }

        while (!q.empty()) {
            std::vector<int> level;
            int level_size = q.size();
            for (int i = 0; i < level_size; i++) {
                TreeNode* cur = q.front();
                q.pop_front();
                level.push_back(cur->val);
                if (cur->left) {
                    q.push_back(cur->left);
                }
                if (cur->right) {
                    q.push_back(cur->right);
                }
            } 
            ans.push_back(level);
        }
        return ans;
    }
};
