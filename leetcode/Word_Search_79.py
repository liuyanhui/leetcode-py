"""
79. Word Search
Medium
--------------------------------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.exist_1(board, word)

    def exist_1(self, board: List[List[str]], word: str) -> bool:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. naive solution
        M=len(board),N=len(board[0]),K=len(word)
        依次遍历每个元素board[i][j]，假设board[i][j]作为第一个字母与word进行匹配；
        每个位置都会引发四个方向的匹配计算，所以时间复杂度为：O((M*N*K)^4)
        2. 图的遍历和查找一般有两种思路DFS和BFS
        上面的"1."是DFS思路。
        本题不适合用BFS。
        3. BFS中是否可以使用缓存？缓存过于复杂，并且需要的较多的存储空间。不适合

        验证通过： 性能较差
        Runtime 6788 ms Beats 10.97%
        Memory 16.58 MB Beats 75.30%
        """

        def dfs(seen: set, i: int, j: int, k: int):
            if k >= len(word):
                return True
            if i < 0 or len(board) <= i or j < 0 or len(board[0]) <= j:
                return False
            key = str(i) + ':' + str(j)
            if key in seen:
                return False
            # 沿4个方向进行匹配
            if board[i][j] == word[k]:
                seen.add(key)
                if (dfs(seen, i, j + 1, k + 1)
                        or dfs(seen, i + 1, j, k + 1)
                        or dfs(seen, i, j - 1, k + 1)
                        or dfs(seen, i - 1, j, k + 1)):
                    return True
                seen.remove(key)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(set(), i, j, 0):
                    return True
        return False


def do_func(board: List[List[str]], word: str, expect: bool):
    ret = Solution().exist(board, word)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED", expect=True)
    do_func(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE", expect=True)
    do_func(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB", expect=False)
    do_func(board=[["A", "B"], ["C", "D"]], word="ABCD", expect=False)


if __name__ == "__main__":
    main()
