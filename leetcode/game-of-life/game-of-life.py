class Solution:
    """
    https://leetcode.com/problems/game-of-life/
    289. Game of Life
    Medium
    --------------------
    According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

    Example:
    Input:
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    Output:
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]

    Follow up:
    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
    """

    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.gameOfLife_2(board)

    def gameOfLife_1(self, board):
        """
        Space complexity is O(M*N).Time complexity is O(M*N)
        The next solution is the improved one which space complexity is O(1),that's owesome.
        :param board:
        :return:
        """
        self.template = [[[i, j] for i in (-1, 0, 1)] for j in (-1, 0, 1)]
        self.template[1][1] = [9999, 9999]
        tmp_board = [[j for j in row] for row in board]

        for i in range(len(tmp_board)):
            for j in range(len(tmp_board[i])):
                count = self.countLiveNeighborsCell(tmp_board, i, j)
                if tmp_board[i][j] == 0 and count == 3:
                    board[i][j] = 1
                elif tmp_board[i][j] == 1 and count < 2:
                    board[i][j] = 0
                # elif tmp_board[i][j] == 1 and count in [2, 3]:
                #     board[i][j] = 1
                elif tmp_board[i][j] == 1 and count > 3:
                    board[i][j] = 0

    def countLiveNeighborsCell(self, board, i, j):
        """
        计算某个cell的live neighbors 数量
        :param board:
        :param i:
        :param j:
        :return:
        """

        def bordervalidate(x, y, max_x, max_y):
            if max_x >= x >= 0 and max_y >= y >= 0:
                return True

        count = 0
        for x in self.template:
            for y in x:
                m = i + y[0]
                n = j + y[1]
                if bordervalidate(m, n, len(board) - 1, len(board[0]) - 1):
                    count += board[m][n]
        return count

    def gameOfLife_2(self, board):
        """
        Space complexity is O(1).Time complexity is O(M*N)
        参考思路:
        https://leetcode.com/problems/game-of-life/solution/
        主要思路:
        1.如果原始值是0,更新后是1,那么记为-1
        2.如果原始值是1,更新后是0,那么记为2
        3.最后把2和-1,分别替换成1和0
        :param board:
        :return:
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        def borderCheck(x, y, m_x, m_y):
            """
            是否越界
            :param x:
            :param y:
            :param m_x:
            :param m_y:
            :return:
            """
            if 0 <= x <= m_x and 0 <= y <= m_y:
                return True

        def countLiveNeighborsCell_2(board, i, j):
            """
            计算neighbor的数量
            :param board:
            :param i:
            :param j:
            :return:
            """
            live_count = 0
            for neighbor in neighbors:
                cross_border = borderCheck(i + neighbor[0], j + neighbor[1], len(board) - 1, len(board[0]) - 1)
                if cross_border and board[i + neighbor[0]][j + neighbor[1]] > 0:
                    live_count += 1
            return live_count

        for i in range(len(board)):
            for j in range(len(board[i])):
                count = countLiveNeighborsCell_2(board, i, j)
                if board[i][j] == 0 and count == 3:
                    board[i][j] = -1
                elif board[i][j] == 1 and count < 2:
                    board[i][j] = 2
                # elif board[i][j] == 1 and count in [2, 3]:
                #     board[i][j] = 1
                elif board[i][j] == 1 and count > 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0


def main():
    a = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    Solution().gameOfLife(a)
    print(a)
    print("-----------------")


if __name__ == "__main__":
    main()
