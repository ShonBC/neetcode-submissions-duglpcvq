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
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* parent = nullptr;
        TreeNode* cur = root;

        // Find key node in tree
        while (cur && cur->val != key) {
            parent = cur;
            if (key < cur->val) {
                cur = cur->left;
            }
            else {
                cur = cur->right;
            }
        }

        // If key not in tree return root
        if (!cur) {
            return root;
        }

        // Single child case
        if (!cur->left || !cur->right) {
            TreeNode* child = cur->left ? cur->left : cur->right;
            if (!parent) return child;
            if (parent->left == cur) {
                parent->left = child;
            }
            else {
                parent->right = child;
            }
            return root;
        }


        // Two children case
        TreeNode* suc = cur;
        TreeNode* suc_child = cur->right;

        while (suc_child->left) {
            suc = suc_child;
            suc_child = suc_child->left;
        }

        // Replace cur node wiht successor's child value
        cur->val = suc_child->val;

        // Remove successors child node
        if (suc->left == suc_child) {
            suc->left = suc_child->right;
        }
        else {
            suc->right = suc_child->right;
        }

        return root;

    }
};