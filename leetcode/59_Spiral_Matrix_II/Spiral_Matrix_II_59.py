"""
59. Spiral Matrix II
Medium
------------------------
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> list:
        return self.generateMatrix_1(n)

    def generateMatrix_1(self, n: int) -> list:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. 总结公式法 or 遍历计算法 or 分层遍历计算法。采用分层遍历计算法。
        2. 分层遍历计算法。每层按照clockwise方向遍历计算，函数为f(i_min,i_max,num_start,layer_size)，每个方向按照左闭右开'[i_min,i_min+layer_size)'的规则进行计算。

        公式法见:
        https://leetcode.com/problems/spiral-matrix-ii/solutions/22282/4-9-lines-python-solutions/

        验证通过:
        Runtime 39 ms Beats 58.05%
        Memory 17.30 MB Beats 23.68%

        Args:
            n:

        Returns:

        """

        def fill_clockwise(i_min: int, i_max: int, start: int, size: int, ret: list):
            if i_min > i_max:
                return
            if i_min == i_max:
                ret[i_min][i_max] = start

            # top , from left to right
            for i in range(size - 1):
                ret[i_min][i_min + i] = start
                start += 1
            # right, from top to bottom
            for i in range(size - 1):
                ret[i_min + i][i_max] = start
                start += 1
            # bottom, from right to left
            if i_min < i_max:
                for i in range(size - 1):
                    ret[i_max][i_max - i] = start
                    start += 1
            # left, from bottom to top
            if i_min < i_max:
                for i in range(size - 1):
                    ret[i_max - i][i_min] = start
                    start += 1

            # next layer
            fill_clockwise(i_min + 1, i_max - 1, start, size - 2, ret)

        ret = [[0 for i in range(n)] for j in range(n)]
        fill_clockwise(0, n - 1, 1, n, ret)
        return ret


def do_func(s: str, expect: list):
    ret = Solution().generateMatrix(s)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    do_func(1, [[1]])
    do_func(4, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    do_func(20, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])


if __name__ == "__main__":
    main()
