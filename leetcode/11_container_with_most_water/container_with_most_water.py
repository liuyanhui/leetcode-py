"""
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water
Medium
--------------------
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2

Constraints:
n = height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104
"""


class Solution:
    def maxArea(self, height):
        return self.maxArea_2(height)

    def maxArea_2(self, height):
        """
        参考思路:
        https://leetcode.com/problems/container-with-most-water/solution/
        双指针夹逼法
        ----------------
        验证通过:
        Runtime: 164 ms, faster than 60.44% of Python3 online submissions for Container With Most Water.
        Memory Usage: 16.6 MB, less than 9.63% of Python3 online submissions for Container With Most Water
        :param height:
        :return:
        """
        if not height:
            return 0
        ret = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ret = max(ret, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ret

    def maxArea_brute(self, height):
        """
        暴力法:
        双重遍历,每两条线之间的面积都计算一遍,取最大值即可
        Time complexity:O(N*N)
        应该不满足要求
        :param height:
        :return:
        """
        if not height:
            return 0
        ret = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                ret = max(ret, min(height[i], height[j]) * (j - i))
        return ret


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ret = Solution().maxArea(height)
    print(ret)
    print(ret == 49)
    print("---------------------")

    height = [1, 1]
    ret = Solution().maxArea(height)
    print(ret)
    print(ret == 1)
    print("---------------------")

    height = [4, 3, 2, 1, 4]
    ret = Solution().maxArea(height)
    print(ret)
    print(ret == 16)
    print("---------------------")

    height = [1, 2, 1]
    ret = Solution().maxArea(height)
    print(ret)
    print(ret == 2)
    print("---------------------")


if __name__ == "__main__":
    main()
