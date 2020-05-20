"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
1351. Count Negative Numbers in a Sorted Matrix
Easy
---------------
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""


class Solution:

    def countNegatives(self, grid):
        return self.countNegatives_2(grid)

    def countNegatives_2(self, grid):
        """
        极简版代码,思路如下:
        https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510267/Python-Different-1-line
        :param grid:
        :return:
        """
        return sum(a < 0 for r in grid for a in r)

    def countNegatives_1(self, grid):
        """
        思路:
        如果 grid[i][j]<0,那么[i:][j:]全部满足条件
        -------
        验证通过:
        Runtime: 140 ms, faster than 16.53% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
        Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
        :param grid:
        :return:
        """
        count = 0
        mj=len(grid[0])
        for i in range(len(grid)):
            for j in range(mj):
                if grid[i][j]<0:
                    count += (len(grid)-i)*(mj-j)
                    mj=j
                    break
        return count


def main():
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    ret = Solution().countNegatives(grid)
    print(ret)
    print(ret == 8)
    print('--------------------')

    grid = [[-1]]
    ret = Solution().countNegatives(grid)
    print(ret)
    print(ret == 1)
    print('--------------------')


if __name__=="__main__":
    main()