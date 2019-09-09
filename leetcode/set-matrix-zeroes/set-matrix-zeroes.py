"""
https://leetcode.com/problems/set-matrix-zeroes/
73. Set Matrix Zeroes
Medium
----------------------------------------------------
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.setZeroes_5(matrix)

    def setZeroes_1(self, matrix):
        """
        创建一个matrix的副本,用来保存原始矩阵.在matrix上进行实际的操作.
        这个方法太普通了,不是想要的结果.
        space complexity O(m*n)
        time complexity O(m*n)
        :param matrix:
        :return:
        """
        pass

    def setZeroes_2(self, matrix):
        """
        需要遍历两次.
        第一次遍历记录都有哪些行,哪些列需要置为0.
        第二次遍历将这些行和列的值置为0
        space complexity O(m+n)
        time complexity O(m*n)
        :param matrix:
        :return:
        """
        if matrix is None:
            return
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0

    def setZeroes_3(self, matrix):
        """
        需要遍历两次.
        第一次,把需要修改的元素设置为极小值.需要注意的是,如果已经=0,不做修改,不能设置为极小值
        第二次,把值为-1的元素设置为0
        space complexity O(1)
        time complexity O(m*n*(m+n))
        :param matrix:
        :return:
        """
        if matrix is None:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for m in range(len(matrix)):
                        if matrix[m][j] != 0:
                            matrix[m][j] = float("inf")
                    for n in range(len(matrix[i])):
                        if matrix[i][n] != 0:
                            matrix[i][n] = float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

    def setZeroes_4(self, matrix):
        """
        方法setZeroes_2和setZeroes_3的优化版本,结合这两者的优点.其中用第一行和第一列代替setZeroes_2中使用的row和col.
        隐含信息:修改行头或者列头的元素时,行头或者列头的元素一定是已经访问过的.从某种程度上保证了只修改已访问过的元素.
        space complexity O(1)
        time complexity O(m*n)
        :param matrix:
        :return:
        """
        if matrix is None:
            return
        col0 = False
        for i in range(len(matrix)):
            # setZeroes_2中row[0]和col[0]是两个元素,本方法中matrix[0][0]是一个元素,需要单独处理
            # matrix[0][0]代表第0行,col0代表第0列
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 此处跟setZeroes_2不同,因为setZeroes_2中row和col是不会被修改的.
        # setZeroes_2中row[0]和col[0]是两个元素,本方法中matrix[0][0]是一个元素,需要单独处理
        # 需要注意列头和行头的元素要最后处理,否则会出错.因为后面的遍历依赖于列头和行头是否==0的结果.
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, -1, -1):
                if j == 0:  # 第0列需要单独处理
                    if col0:
                        matrix[i][j] = 0
                else:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

    def setZeroes_5(self, matrix):
        """
        方法setZeroes_4的另一种版本,不是从大到小的遍历.而是从小到大遍历之后再处理第0列和第0行
        space complexity O(1)
        time complexity O(m*n)
        :param matrix:
        :return:
        """
        if matrix is None:
            return
        col0 = False
        for i in range(len(matrix)):
            # setZeroes_2中row[0]和col[0]是两个元素,本方法中matrix[0][0]是一个元素,需要单独处理
            # matrix[0][0]代表第0行,col0代表第0列
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 此处跟setZeroes_2不同,因为setZeroes_2中row和col是不会被修改的.
        # setZeroes_2中row[0]和col[0]是两个元素,本方法中matrix[0][0]是一个元素,需要单独处理
        # 需要注意列头和行头的元素要最后处理,否则会出错.因为后面的遍历依赖于列头和行头是否==0的结果.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第0行和第0列的顺序不能弄反,因为处理第0列会修改matrix[0][0]的值
        # 处理第0行
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # 单独处理第0列
        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0



def main():
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
    # print("------------------")

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
    print("------------------")

    matrix = [[-1], [2], [3]]
    Solution().setZeroes(matrix)
    print(matrix)
    print("------------------")

    matrix = [[-4, -2147483648, 6, -7, 0],
              [-8, 6, -8, -6, 0],
              [2147483647, 2, -9, -6, -10]]
    Solution().setZeroes(matrix)
    print(matrix)
    print("------------------")

    matrix = [[1, 1, 1],
              [0, 1, 2]]
    Solution().setZeroes(matrix)
    print(matrix)
    print("------------------")


if __name__ == "__main__":
    main()
