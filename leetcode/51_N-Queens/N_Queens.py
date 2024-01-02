"""
51. N-Queens
Hard
--------------------------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int):
        return self.solveNQueens_1(n)

    def solveNQueens_1(self, n: int):
        """
        Thinking：
        1.naive solution
        1.1. 递归+穷举
        1.2. 按行计算，每行都必然有一个queen，故所有行计算完成时，可以返回一个结果。
        1.3. 需要实现checkRow(),checkCol(),checkSlash(),checkBackslash()

        验证通过:
        Runtime 87 ms Beats 32.07% of users with Python3
        Memory 17.71 MB Beats 16.20% of users with Python3
        :param n:
        :return:
        """
        ret = []
        board = [["." for i in range(n)] for j in range(n)]
        self.helper(board, 0, ret)
        return ret

    def helper(self, board, i, ret):
        if i == len(board):
            # review 序列化二维数组
            ret.append(["".join(item) for item in board]);
        for j in range(len(board[0])):
            if self.check_col(board, j) and self.check_slash(board, i, j) and self.check_backslash(board, i, j):
                board[i][j] = "Q"
                self.helper(board, i + 1, ret)
                board[i][j] = "."

    def check_col(self, board, j):
        for i in range(len(board)):
            if board[i][j] == "Q":
                return False
        return True

    def check_slash(self, board, i, j):
        # forward to top and right
        x, y = i - 1, j + 1
        while 0 <= x and y <= len(board[0]) - 1:
            if board[x][y] == "Q":
                return False
            else:
                x -= 1
                y += 1
        # forward to bottom and left
        x, y = i + 1, j - 1
        while x <= len(board) - 1 and 0 <= y:
            if board[x][y] == "Q":
                return False
            else:
                x += 1
                y -= 1

        return True

    def check_backslash(self, board, i, j):
        # forward to top and left
        x, y = i - 1, j - 1
        while 0 <= x and 0 <= y:
            if board[x][y] == "Q":
                return False
            else:
                x -= 1
                y -= 1
        # forward to bottom and right
        x, y = i + 1, j + 1
        while x <= len(board) - 1 and y <= len(board[0]) - 1:
            if board[x][y] == "Q":
                return False
            else:
                x += 1
                y += 1
        return True


def main():
    ret = Solution().solveNQueens(4)
    print(ret)
    print(ret == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    print("---------------------")
    pass


if __name__ == "__main__":
    main()
