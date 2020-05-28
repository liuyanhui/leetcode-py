"""
https://leetcode.com/problems/search-a-2d-matrix/
74. Search a 2D Matrix
Medium
-------------
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target):
        pass

    def searchMatrix_2(self, matrix, target):
        """
        也可以不把matrix看成二维数组,因为二维数据是自增的,所以使用一次二分查也可以
        验证通过,
        Runtime: 68 ms, faster than 63.31% of Python3 online submissions for Search a 2D Matrix.
        Memory Usage: 15.6 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix_1(self, matrix, target):
        """
        思路:两次二分查找,需要注意的是第一次查找的结果是"找出自增序列中小于target的最大值"
        ----------
        验证通过,
        Runtime: 72 ms, faster than 37.29% of Python3 online submissions for Search a 2D Matrix.
        Memory Usage: 15.7 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l, r = 0, len(matrix) - 1
        # 第一次二分查找,找出row
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        row = l
        # 需要判断row
        if row > 0 and matrix[row][0] > target > matrix[row - 1][0]:
            row -= 1
        # 第二次二分查找
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == True)
    print('--------------------')

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == True)
    print('--------------------')

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 130
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = -130
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    matrix = [
        [1, 3, 5, 7]
    ]
    target = -130
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')


if __name__ == "__main__":
    main()
