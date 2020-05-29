"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
240. Search a 2D Matrix II
Medium
-------------
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        return self.searchMatrix_2(matrix, target)

    def searchMatrix_2(self, matrix, target):
        """
        O(M+N)的解法,
        参考思路:
        https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
        https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66168/4-lines-C-6-lines-Ruby-7-lines-Python-1-liners
        简述如下:
        1.从左下开始遍历,当matrix[i][j]>target时,i--;否则,j++.
        2.直到matrix[i][j]==target时,返回True;当发生i越界或j越界时,返回False
        也可以从右上开始遍历.但是不可以从左上和右下开始遍历,因为这两个位置往任何一个方向遍历要么都是递增的,要么都是递减的.
        ---------
        验证通过:
        Runtime: 40 ms, faster than 53.93% of Python3 online submissions for Search a 2D Matrix II.
        Memory Usage: 18.5 MB, less than 7.41% of Python3 online submissions for Search a 2D Matrix II.
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        i, j = 0, len(matrix[0]) - 1
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

    def searchMatrix_error(self, matrix, target):
        """
        有时间复杂度为O(M+N)的解法.
        思路为:依次根据上,右,下,左进行遍历,其中上和左的边界都是最小值,右和下的边界都是最大值.当最大值<t或最小值>t时,排除该行或该列.以此不断循环.
        验证失败
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        # 切割后行的最小值和最大值
        mii, mai = 0, len(matrix) - 1
        # 切割后列的最小值和最大值
        mij, maj = 0, len(matrix[0]) - 1

        while mii <= mai or mij <= maj:
            if matrix[mii][mij] == target:
                return True
            # 处理上部边界
            for i in range(mij, maj + 1):
                if matrix[mii][i] > target:
                    maj = i - 1
                    break
            # 处理右部边界
            for i in range(mii, mai + 1):
                if matrix[i][maj] < target:
                    mii = i + 1
                else:
                    break
            # 处理下部边界
            for i in range(mij, maj + 1):
                if matrix[mai][i] < target:
                    mij = i + 1
                else:
                    break
            # 处理左部边界
            for i in range(mii, mai + 1):
                if matrix[i][mij] > target:
                    mai = i - 1
                    break
        return False

    def searchMatrix_1(self, matrix, target):
        """
        思路:每一行都用binary search进行查找.
        Time Complexity : O(M*logN)
        验证通过:
        Runtime: 32 ms, faster than 89.62% of Python3 online submissions for Search a 2D Matrix II.
        Memory Usage: 18.5 MB, less than 7.41% of Python3 online submissions for Search a 2D Matrix II.
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False


def main():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == True)
    print('--------------------')

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 20
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = -22
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    matrix = []
    target = 0
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    matrix = [[5, 6, 9], [9, 10, 11], [11, 14, 18]]
    target = 9
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == True)
    print('--------------------')


if __name__ == "__main__":
    main()
