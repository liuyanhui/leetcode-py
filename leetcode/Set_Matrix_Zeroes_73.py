"""
73. Set Matrix Zeroes
Medium
----------------------------------------------------
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.setZeroes_6(matrix)

    def setZeroes_6(self, matrix: list) -> None:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：
        1. copy on write 的思路，在一个新的matrix上进行结果存储。
        Space Complexity: O(m*n)
        2. 遍历matrix，把需要改为0的row[]和col[]记录下来，再修改原始matrix。
        Space Complexity: O(m+n)
        3. 两次遍历
        3.1. 第一次遍历把需要修改的元素改成一个固定值t(matrix[i][j]=t)，第二次遍历，如果matrix[i][j]==t，那么matrix[i][j]=0。
        3.2. matrix[i][j]==0时不修改。
        3.3. 难点是如何选择t的值
        Space Complexity: O(1)
        4. 在3.的基础上优化。用第0行和第0列记录是否需要将对应的行或列全部修改为0。
        4.1. 第0行和第0列需要单独考虑

        验证通过:
        Runtime 103 ms Beats 61.69%
        Memory 17.59 MB Beats 60.12%
        """
        row_0, col_0 = 1, 1  # 记录第0行和第0列是否需要置为0
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                col_0 = 0
                break
        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                row_0 = 0
                break

        # 第一次遍历。先在第0行和第0列标识需要修改的元素
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 第二次遍历。
        # 先不计算matrix[0][0]
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        # 单独计算第0行和第0列
        if col_0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row_0 == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0


def do_func(matrix: list, expect: list):
    Solution().setZeroes(matrix)
    print(matrix)
    print(matrix == expect)
    print("---------------------")


def main():
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    expect = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    do_func(matrix, expect)

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    expect = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]
    do_func(matrix, expect)

    matrix = [[-1], [2], [3]]
    expect = [[-1], [2], [3]]
    do_func(matrix, expect)

    matrix = [
        [-4, -2147483648, 6, -7, 0],
        [-8, 6, -8, -6, 0],
        [2147483647, 2, -9, -6, -10]
    ]
    expect = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [2147483647, 2, -9, -6, 0]
    ]
    do_func(matrix, expect)

    matrix = [
        [1, 1, 1],
        [0, 1, 2]
    ]
    expect = [
        [0, 1, 1],
        [0, 0, 0]
    ]
    do_func(matrix, expect)

    matrix = [[1, 0]]
    expect = [[0, 0]]
    do_func(matrix, expect)


if __name__ == "__main__":
    main()
