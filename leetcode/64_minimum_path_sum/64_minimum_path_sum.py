"""
https://leetcode.com/problems/minimum-path-sum/
64. Minimum Path Sum
Medium
类似的题目:
https://www.geeksforgeeks.org/min-cost-path-dp-6/
------------
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        return self.minPathSum_2(grid)

    def minPathSum_2(self, grid: list) -> int:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. 递归法，比较每种可能，得到最优解
        时间复杂度：O(2^N)
        2. DP法
        dp[i][j]为grid[i][j]的最小值
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        时间复杂度：O(N^N)

        Runtime 70 ms Beats 99.41%
        Memory 18.58 MB Beats 58.72%

        Args:
            grid:

        Returns:

        """
        dp = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        for i in range(2, len(grid) + 1):
            dp[i][0] = 9999
        for j in range(2, len(grid[0]) + 1):
            dp[0][j] = 9999

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[-1][-1]

    def minPathSum_brute(self, grid: list) -> int:
        """
        暴力法,用dfs的思路从左上到右下进行遍历,并计算min_sum
        使用BUD方法进行改进:
        1.记录(i,j)到(m,n)的最小值于local_optimal[m,n]中,可以避免重复查询局部最优解
        :param gird:
        :return:
        """
        pass

    def minPathSum_dp(self, grid: list) -> int:
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

    def minPathSum_1(self, grid):
        """
        代码简化版本,
        https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


def do_func(grid: list, expect: int):
    ret = Solution().minPathSum(grid)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)
    do_func([[1, 2, 3], [4, 5, 6]], 12)
    do_func([[1, 2], [1, 1]], 3)


if __name__ == "__main__":
    main()
