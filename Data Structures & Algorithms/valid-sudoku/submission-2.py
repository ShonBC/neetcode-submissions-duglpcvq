class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num != '.':
                    if num in rows[row]: return False
                    rows[row].add(num)

                    if num in cols[col]: return False
                    cols[col].add(num)

                    if num in boxes[(row//3, col//3)]: return False
                    boxes[(row//3, col//3)].add(num)
                    
        return True