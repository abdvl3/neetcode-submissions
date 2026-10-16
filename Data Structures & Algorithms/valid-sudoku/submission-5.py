class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenC = defaultdict(list)
        seenS = defaultdict(list)

        for row in range (0,9):
            seen = []
            for col in range (0,9):
                print(seen)
                cur = board[row][col]
                square = (row // 3) * 3 + col // 3

                if cur != '.':

                    if cur in seen:
                        return False
                    seen.append(cur)

                    if cur in seenC[col]:
                        return False
                    seenC[col].append(cur)

                    
                    if cur in seenS[square]:
                        return False
                    seenS[square].append(cur)

        return True