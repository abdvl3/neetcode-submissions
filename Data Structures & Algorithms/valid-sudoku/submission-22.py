class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        checkedC = [[]for i in range(0,9)]
        checkedS = [[]for i in range(0,9)]

        for row in range (0,9):
            checkedR = []
            for col in range(0,9):
                # goes through row and does checks
                cur = board[row][col]
                if cur == '.':
                    continue
                if cur in checkedR:
                    return False
                checkedR.append(cur)
                # populates and checks array for columns
                if cur in checkedC[col]:
                    return False
                checkedC[col].append(cur)
                # populates and checks array for squares
                square = (row // 3)*3 + (col // 3)
                print(row,(row//3)*3,col//3,col)
                if cur in checkedS[square]:
                    return False
                checkedS[square].append(cur)

        return True

            
