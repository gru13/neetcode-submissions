class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # let me check every row and column 
        for i in range(9):
            r = []
            c = [] 
            for j in range(9):
                if board[i][j] != ".":
                    r.append(board[i][j]) 
                if board[j][i] != ".":
                    c.append(board[j][i])
                
            if len(r) != len(set(r)) or len(c) != len(set(c)):
                return False
        
        # now every box 
        for i in range(9):
            ranA = 3*(i//3) 
            ranB = 3*(i%3)
            print((ranA, ranB))
            box = [] 
            for a in range(ranA, ranA + 3):
                for b in range(ranB, ranB + 3):
                    if board[a][b] != ".":
                        box.append(board[a][b]) 
            print(box)
            if len(box) != len(set(box)):
                return False
            
        return True