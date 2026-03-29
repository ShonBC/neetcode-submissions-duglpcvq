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
    vector<int> rightSideView(TreeNode* root) {
        deque<TreeNode*> q;
        vector<int> ans;
        if (!root) {
            return ans;
        }
        q.push_back(root);
        while (!q.empty()) {
            vector<int> level;
            int level_size = q.size();
            for (int i = 0; i < level_size; i++) {
                TreeNode* cur = q.front();
                q.pop_front();
                if (i == level_size - 1) {
                    ans.push_back(cur->val);
                }
                if (cur->left) {
                    q.push_back(cur->left);
                }
                if (cur->right) {
                    q.push_back(cur->right);
                }
            }
        }
        return ans;
    }
};
