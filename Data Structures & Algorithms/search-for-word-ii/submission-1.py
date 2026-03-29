class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''find index of letter that hasnt been visited
        explore vertical and horizontal for children
        '''
        moves = ((0,1), (0,-1), (1,0), (-1,0))
        visited = set()
        ans = []
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node, word) -> None:
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or board[r][c] not in node.children):
                
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word and word not in ans:
                ans.append(word)
                
            
            for mr, mc in moves:
                dfs(r + mr, c + mc, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, '')
        
        return ans