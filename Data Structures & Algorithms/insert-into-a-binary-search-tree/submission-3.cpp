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
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* node = new TreeNode(val);
        if (!root) return node;
        TreeNode* cur = root; 
        while (true) {
            if (val < cur->val) {
                if (!cur->left) {
                    cur->left = node;
                    return root;
                }
                cur = cur->left;
            }
            else {
                if (!cur->right) {
                    cur->right = node;
                    return root;
                }
                cur = cur->right;
            }
        }
    }
};