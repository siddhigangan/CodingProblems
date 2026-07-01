class Solution:
    # Added 'self' as the first parameter
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        r0, c0 = 0, 0  # Good practice to initialize coordinates
        
        # 1. Find the white rook ('R')
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r0, c0 = i, j
                    break
                    
        # 2. Check all 4 cardinal directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            r, c = r0 + dr, c0 + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'p':  # Found a black pawn
                    ans += 1
                    break
                if board[r][c] != '.':  # Hit a bishop or another piece
                    break
                r += dr
                c += dc
                
        return ans
