class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = len(board),len(board[0])
        for r in range(rows):
            seen = set()
            for c in range(cols):
                if board[r][c]==".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        for c in range(cols):
            seen = set()
            for r in range(rows):
                if board[r][c]==".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                seen = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True
        