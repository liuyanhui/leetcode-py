"""
54. Spiral Matrix
Medium
------------------------
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: list) -> list:
        return self.spiralOrder_2(matrix)

    def spiralOrder_2(self, matrix: list) -> list:
        """
        Round 3
        Score[1] Lower is harder

        Thinking:
        1.与spiralOrder_1()不同,非递归的一种简单实现
        1.1. 采用[[0,1][1,0][0,-1][-1,0]]四种计算方式进行遍历

        验证通过:
        43 ms Beats 28.42%
        17.26 MB Beats 27.69%

        Args:
            matrix:

        Returns:

        """
        ret = []
        xmin, xmax = 0, len(matrix) - 1
        ymin, ymax = 0, len(matrix[0]) - 1
        delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direct = 0  # direct=0 对应 delta[0],依次类推

        i, j = 0, 0
        while xmin <= xmax and ymin <= ymax:
            while xmin <= i <= xmax and ymin <= j <= ymax:
                ret.append(matrix[i][j]);
                i += delta[direct][0]
                j += delta[direct][1]
            if direct == 0:
                direct = 1
                xmin += 1
                i = xmin
                j = ymax
            elif direct == 1:
                direct = 2
                ymax -= 1
                j = ymax
                i = xmax
            elif direct == 2:
                direct = 3
                xmax -= 1
                i = xmax
                j = ymin
            elif direct == 3:
                direct = 0
                ymin += 1
                j = ymin
                i = xmin

            if xmin > xmax and ymin > ymax:
                break

        return ret

    def spiralOrder_1(self, matrix: list) -> list:
        """
        Round 3
        Score[1] Lower is harder

        Thinking：
        1.naive solution
        按序迭代计算，每次迭代更新边界
        2.递归思路
        按层递归，每层为一圈
        3.一个非常简单的理解、和简单的实现
        https://leetcode.com/problems/spiral-matrix/solutions/20571/1-liner-in-python-ruby/

        验证通过:
        42 ms Beats 35.82%
        17.42 MB Beats 5.53%

        Args:
            matrix:

        Returns:

        """
        ret = []

        def helper(matrix: list, r0: int, r1: int, c0: int, c1: int):
            if r0 > r1 or c0 > c1:
                return
            # review 向右和向下不会出现重复计算,所以不用判断下标是否越界.
            # review 由于二维数组m*n且m!=n,所以采用横向闭区间,纵向开区间的方式更简单.
            # from left to right ,[c0,c1],闭区间
            for i in range(c0, c1 + 1):
                ret.append(matrix[r0][i])
            r0 += 1
            # from top to bottom,(r0,r1),开区间
            for i in range(r0, r1):
                ret.append(matrix[i][c1])
            c1 -= 1
            # from right to left,[c0,c1],闭区间
            if r0 <= r1:
                for i in range(c1 + 1, c0 - 1, -1):
                    ret.append(matrix[r1][i])
                r1 -= 1
            # from bottom to top,(),开区间
            if c0 <= c1:
                for i in range(r1, r0 - 1, -1):
                    ret.append(matrix[i][c0])
                c0 += 1
            helper(matrix, r0, r1, c0, c1)

        helper(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)

        return ret


def do_func(matrix: list, expect: list):
    ret = Solution().spiralOrder(matrix)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
    do_func([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    do_func([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    do_func([[1]], [1])
    do_func([[]], [])
    do_func([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    do_func([[2, 5, 8], [4, 0, -1]], [2, 5, 8, -1, 0, 4])
    do_func([[2, 5, 8]], [2, 5, 8])
    do_func([[1, 2], [3, 4]], [1, 2, 4, 3])
    do_func([[3], [2]], [3, 2])
    do_func([[3], [2], [1]], [3, 2, 1])


if __name__ == '__main__':
    main();
