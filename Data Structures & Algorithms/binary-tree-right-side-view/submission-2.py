# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            level_size = len(q)
            for i in range(level_size):
                cur = q.popleft()
                if i == level_size - 1:
                    ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)            
            
        return ans