from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):  # 行
            s = set()
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in s:
                    return False
                s.add(board[i][j])

        for i in range(9):  # 列
            s = set()
            for j in range(9):
                if board[j][i].isdigit() and board[j][i] in s:
                    return False
                s.add(board[j][i])

        for r in range(0, 7, 3):  # 0,0,  0,3, 0, 6
            for c in range(0, 7, 3):
                s = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        print('rc ', r, '  ', c, '  [i,j] ', i, ' ', j)
                        if board[i][j].isdigit() and board[i][j] in s:
                            return False
                        s.add(board[i][j])

        return True


# for r in range(0, 7, 3):  # 0,0,  0,3, 0, 6
#     for c in range(0, 7, 3):
#         print('rc ', r, '  ', c)

s = Solution()
b = s.isValidSudoku([
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]])

print(b)
