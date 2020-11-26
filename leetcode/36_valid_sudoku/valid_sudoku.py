"""
https://leetcode.com/problems/valid-sudoku/
36. Valid Sudoku
Medium
---------------------
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""


class Solution:
    def isValidSudoku(self, board):
        return self.isValidSudoku_2(board)

    def isValidSudoku_2(self, board):
        """
        one pass 方案
        参考思路:https://leetcode.com/problems/valid-sudoku/solution/
        用户空间换时间
        验证通过:
        Runtime: 112 ms, faster than 11.26% of Python3 online submissions for Valid Sudoku.
        Memory Usage: 14.4 MB, less than 6.31% of Python3 online submissions for Valid Sudoku.
        :param board:
        :return:
        """
        if not board or len(board) != 9:
            return False
        row = [{} for i in range(0, 10)]
        col = [{} for i in range(0, 10)]
        box = [{} for i in range(0, 10)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    value = int(board[i][j])
                    row[i][value] = row[i].get(value, 0) + 1
                    col[j][value] = col[j].get(value, 0) + 1
                    box[i // 3 * 3 + j // 3][value] = box[i // 3 * 3 + j // 3].get(value, 0) + 1

                    if row[i][value] > 1 or col[j][value] > 1 or box[i // 3 * 3 + j // 3][value] > 1:
                        return False
        return True

    def isValidSudoku_1(self, board):
        """
        思路:
        1.按行判断
        2.按列判断
        3.按3*3九宫格判断
        这种思路需要整体遍历3次.有没有只遍历一次的办法呢?
        验证通过:
        Runtime: 96 ms, faster than 58.52% of Python3 online submissions for Valid Sudoku.
        Memory Usage: 14.4 MB, less than 5.74% of Python3 online submissions for Valid Sudoku.
        :param board:
        :return:
        """
        if not board or len(board) != 9:
            return False
        # 行
        for i in range(0, 9):
            existed = [0] * 9
            for j in range(0, 9):
                cell = board[i][j]
                if cell != ".":
                    if existed[int(cell) - 1] > 0:
                        return False
                    else:
                        existed[int(cell) - 1] = 1
        # 列
        for i in range(0, 9):
            existed = [0] * 9
            for j in range(0, 9):
                cell = board[j][i]
                if cell != ".":
                    if existed[int(cell) - 1] > 0:
                        return False
                    else:
                        existed[int(cell) - 1] = 1
        # sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                existed = [0] * 9
                for k in range(0, 9):
                    cell = board[i + k // 3][j + k % 3]
                    if cell != ".":
                        if existed[int(cell) - 1] > 0:
                            return False
                        else:
                            existed[int(cell) - 1] = 1
        return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ret = Solution().isValidSudoku(board)
    print(ret)
    print(ret == True)
    print("---------------------")

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ret = Solution().isValidSudoku(board)
    print(ret)
    print(ret == True)
    print("---------------------")


if __name__ == "__main__":
    main()
