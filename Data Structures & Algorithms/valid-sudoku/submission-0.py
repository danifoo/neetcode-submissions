class Solution:
    def convertToInt(self, s: str) -> int:
        if s == ".":
            return 0

        return int(s)

    def areAllRowsValid(self, board: List[List[str]]) -> bool:
        
        for row in board:
            rowMap = set()
            for cell in row:
                cellNum = self.convertToInt(cell)
                if cellNum == 0:
                    continue
                elif cellNum in rowMap:
                    return False
                else:
                    rowMap.add(cellNum)
        
        return True

    def areAllColsValid(self, board: List[List[str]]) -> bool:
        
        for col in range(0, 9):
            colMap = set()
            for cell in range(0, 9):
                cellNum = self.convertToInt(board[cell][col])
                if cellNum == 0:
                    continue
                elif cellNum in colMap:
                    return False
                else:
                    colMap.add(cellNum)        
        return True

    def areAllGridsValid(self, board: List[List[str]]) -> bool:
        for rowStart in range(0, 9, 3):
            for colStart in range(0, 9, 3):
                gridMap = set()
                for gridRow in range(0, 3):
                    for gridCol in range(0, 3):
                        cellNum = self.convertToInt(board[rowStart + gridRow][colStart + gridCol])
                        if cellNum == 0:
                            continue
                        elif cellNum in gridMap:
                            return False
                        else:
                            gridMap.add(cellNum)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if self.areAllRowsValid(board) and self.areAllColsValid(board) and self.areAllGridsValid(board):
            return True

        return False
        