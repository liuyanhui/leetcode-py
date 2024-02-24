"""
74. Search a 2D Matrix
Medium
-------------
You are given an m x n integer matrix matrix with the following two properties:
 - Each row is sorted in non-decreasing order.
 - The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        return self.searchMatrix_3(matrix, target)

    # review 思路1,可以参考:74_search_a_2d_matrix.searchMatrix_2()
    def searchMatrix_3(self, matrix: list, target: int) -> bool:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. Binary Search的变种
        假设m*n的matrix，查找的起点为[r1,c1]，终点为[r2,c2]
        可知区间内数的数量为：T=(c2+1)+(m-r1+1)+(r2-r1-1)*m
        2. 先通过对第0列数字进行Binary Search定位到行i，再通过对第i行进行Binary Search查找target

        本方案采用思路2.
        review 思路1,可以参考:74_search_a_2d_matrix.searchMatrix_2()

        验证通过:
        Runtime 51 ms Beats 29.66%
        Memory 17.02 MB Beats 88.26%
        """
        m, n = len(matrix), len(matrix[0])
        # 对第0列数字进行Binary Search定位到行
        l, r = 0, m - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] < target:
                if matrix[mid][n - 1] < target:
                    l = mid + 1
                else:
                    l = r = mid
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                return True
        # 对第i行进行Binary Search查找target
        i = l
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[i][mid] < target:
                l = mid + 1
            elif target < matrix[i][mid]:
                r = mid - 1
            else:
                return True
        return False


def do_func(matrix: list, target: int, expect: bool):
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 130, False)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], -130, False)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True)
    do_func([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 10, True)
    do_func([[1, 3, 5, 7]], 1, True)
    do_func([[1, 3, 5, 7]], -130, False)


if __name__ == "__main__":
    main()
