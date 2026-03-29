# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        parent = None
        cur = root
        # Find Node to delete
        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        # Return root if key is not in tree
        if not cur:
            return root

        # Cur node has one or no children
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
            return root

        # Node with two children
        # Find in-order successor and its parent
        par_r = cur # Parent of right subrtee min node
        l_step = cur.right

        # Step left and track right node of the parent
        while l_step.left:
            par_r = l_step
            l_step = l_step.left
        
        # Replace cur's value with successor's val
        cur.val = l_step.val

        # Remove successor node 
        if par_r.left == l_step:
            par_r.left = l_step.right
        else:
            par_r.right = l_step.right
        
        return root
            