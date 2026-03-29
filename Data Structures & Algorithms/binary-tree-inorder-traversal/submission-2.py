# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def search(root):
            if not root:
                return ans
            search(root.left)
            ans.append(root.val)
            search(root.right)
            return ans
        return search(root)            