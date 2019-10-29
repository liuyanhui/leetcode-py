"""
https://leetcode.com/problems/minimum-path-sum/
64. Minimum Path Sum
Medium
类似的题目:
https://www.geeksforgeeks.org/min-cost-path-dp-6/
------------
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid):
        return self.minPathSum_dp(grid)

    def minPathSum_brute(self, grid):
        """
        暴力法,用dfs的思路从左上到右下进行遍历,并计算min_sum
        使用BUD方法进行改进:
        1.记录(i,j)到(m,n)的最小值于local_optimal[m,n]中,可以避免重复查询局部最优解
        :param gird:
        :return:
        """
        pass

    def minPathSum_dp(self, grid):
        """
        采用DP思路
        反向求出(i,j)到(m,n)的最小值保存在local_optimal[m,n]中,最终min(0,0)的值就是解
        推导公式为:local_optimal[i,j]=grid[i,j]+min(local_optimal[i-i,j],local_optimal[i,j-1])
        其中右下角的初始值为local_optimal[m-1,n-1]=grid[m-1,n-1]
        :param gird:
        :return:
        """
        if not grid or len(grid) == 0:
            return 0
        local_optimal = [[0 for cell in row] for row in grid]
        m, n = len(grid), len(grid[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    local_optimal[i][j] = grid[m - 1][n - 1]
                else:
                    if i == m - 1:
                        down = 99999
                    else:
                        down = local_optimal[i + 1][j]
                    if j == n - 1:
                        right = 99999
                    else:
                        right = local_optimal[i][j + 1]
                    local_optimal[i][j] = grid[i][j] + min(right, down)

        return local_optimal[0][0]


def main():
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    ret = Solution().minPathSum(grid)
    print(ret)


if __name__ == "__main__":
    main()
