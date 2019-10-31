"""
https://leetcode.com/problems/number-of-islands/
200. Number of Islands
Medium
类似:https://www.geeksforgeeks.org/find-number-of-islands/
----------------------
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""


class Solution:
    def numIslands(self, grid):
        return self.numIslands_1(grid)

    def numIslands_1(self, grid):
        """
        1.采用dfs遍历,顺时针或逆时针
        2.遍历后的grid值修改为-n,其中n表示iland的编号
        3.遍历每个节点直到结束,如果grid[i][j]<0表示已经归属某个iland,跳过该节点
        :param grid:
        :return:
        """
        if not grid or len(grid[0]) == 0:
            return 0

        def traverse_clockwise(matrix, m, n, cnt):
            # if m < 0 or n < 0 or m > len(matrix) or n < len(matrix[0]):
            #     return
            if matrix[m][n] != "1":
                return
            matrix[m][n] = str(-cnt)
            # 顺时针,从3点方向开始
            if n + 1 < len(matrix[0]):
                traverse_clockwise(matrix, m, n + 1, cnt)
            # 6点方向
            if m + 1 < len(matrix):
                traverse_clockwise(matrix, m + 1, n, cnt)
            # 9点方向
            if n - 1 >= 0:
                traverse_clockwise(matrix, m, n - 1, cnt)
            # 12点方向
            if m - 1 >= 0:
                traverse_clockwise(matrix, m - 1, n, cnt)

        iland_no = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    iland_no += 1
                    traverse_clockwise(grid, i, j, iland_no)
        return iland_no


def main():
    a = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]
    ret = Solution().numIslands(a)
    print(ret)
    print("---------------")

    a = [["1", "1", "0", "0", "0"],
         ["1", "1", "0", "1", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "1", "0"]]
    ret = Solution().numIslands(a)
    print(ret)
    print("---------------")

    a = [["1"]]
    ret = Solution().numIslands(a)
    print(ret)
    print("---------------")


if __name__ == "__main__":
    main()
