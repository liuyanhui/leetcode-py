"""
52. N-Queens II
Hard
------------------------------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.totalNQueens_1(n)

    def totalNQueens_1(self, n: int) -> int:
        """
        Round 3
        Score[2] Lower is harder

        类似51. N-Queens的解决方案,实现略有差别.
        主要是slash和backslash方向的校验有变化.这两个方向上分别有2n-1条线,可以用两个数组array[2n-1]分别保存它们的queen出现情况.
        即,slash[k]==1时表示该条slash已经存在queen,backslash[k]==1时表示该条backslash已经存在queen.
        k是从左向右的方向.
        slash的下标i的计算规则为:
            k=i+j,i和j为棋盘的cell的下标
        backslash的下标i的计算规则为:
            k=n-1-(i-j), i和j为棋盘的cell的下标

        验证通过:
        Runtime 43 ms Beats 87.57% of users with Python3
        Memory 17.46 MB Beats 6.72% of users with Python3

        """
        # 分别保存列,斜线,反斜线的queen出现情况
        col, slash, backslash = [False] * n, [False] * 2 * n, [False] * 2 * n

        def helper(i: int):
            if i == n and n > 0:
                return 1
            ret = 0
            for j in range(n):
                if not col[j] and not slash[i + j] and not backslash[n - 1 - (i - j)]:
                    col[j] = slash[i + j] = backslash[n - 1 - (i - j)] = True
                    ret += helper(i + 1)
                    col[j] = slash[i + j] = backslash[n - 1 - (i - j)] = False
            return ret

        return helper(0)


def do_func(n: int, expect: int):
    ret = Solution().totalNQueens(n)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(4, 2)
    do_func(8, 92)
    do_func(9, 352)


if __name__ == "__main__":
    main()
