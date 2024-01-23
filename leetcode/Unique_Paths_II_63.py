"""
63. Unique Paths II
Medium
-------------------------------
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        return self.uniquePathsWithObstacles_2(obstacleGrid)

    def uniquePathsWithObstacles_2(self, obstacleGrid: list) -> int:
        """
        优化为一维DP数组

        验证通过:
        
        Args:
            obstacleGrid:

        Returns:

        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[j] = obstacleGrid[i - 1][j - 1] ^ 1
                elif obstacleGrid[i - 1][j - 1] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[n]

    def uniquePathsWithObstacles_1(self, obstacleGrid: list) -> int:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. DP思路，dp[i][j]表示从grid[0][0]到grid[i][j]的路线数量
        公式为：
        dp[0][0]=0
        # 第一行
        IF grid[i][0]==1 THEN dp[i][0]=1 ELSE dp[i][0]=0
        # 第一列
        IF grid[0][j]==1 THEN dp[0][j]=1 ELSE dp[0][j]=0
        # 其他
        IF grid[i][j]==1 THEN dp[i][j]=dp[i-1][j]+dp[i][j-1]
        ELSE dp[i][j]=0

        验证通过:
        Runtime 35 ms Beats 98.32%
        Memory 16.54 MB Beats 68.55%

        Args:
            obstacleGrid:

        Returns:

        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j] = obstacleGrid[i - 1][j - 1] ^ 1
                elif obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]


def do_func(obstacleGrid: list, expect: int):
    ret = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2)
    do_func([[0, 1], [0, 0]], 1)
    do_func([[1]], 0)
    do_func([[0]], 1)


if __name__ == "__main__":
    main()
