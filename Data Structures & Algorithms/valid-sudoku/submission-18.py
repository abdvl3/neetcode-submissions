class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seenC = defaultdict(list)
        seenS = [[] for i in range (0,9)]

        for row in range (len(board)):
            seenR = set()
            for column in range(len(board[row])):
                cur = board[row][column]

                if cur == '.':
                    continue
                    
                if cur in seenR:
                    return False
                seenR.add(cur)

                if cur in seenC[column]:
                    return False
                seenC[column].append(cur)

                square = row // 3 * 3 + column // 3

                if cur in seenS[square]:
                    return False
                seenS[square].append(cur)

        return True