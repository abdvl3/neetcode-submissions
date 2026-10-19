class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkedC = [[]for i in range (9)]
        checkedS = [[]for i in range (9)]

        for row in range (9):
            checkedR = []
            for col in range (9):
                cur = board[row][col]
                
                if cur == '.':
                    continue

                if cur in checkedR:
                    return False
                checkedR.append(cur)

                if cur in checkedC[col]:
                    return False
                checkedC[col].append(cur)

                square = (row // 3)*3 + (col // 3)

                if cur in checkedS[square]:
                    return False
                checkedS[square].append(cur)

        return True
