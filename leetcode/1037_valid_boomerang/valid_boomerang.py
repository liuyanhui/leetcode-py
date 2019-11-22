"""
https://leetcode.com/problems/valid-boomerang/
1037. Valid Boomerang
Easy
--------------------
A boomerang is a set of 3 points that are all distinct and not in a straight line.
Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: [[1,1],[2,2],[3,3]]
Output: false

Note:
points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""


class Solution:
    def isBoomerang(self, points):
        return self.isBoomerang_1(points)

    def isBoomerang_1(self, points):
        """
        参考思路:
        https://leetcode.com/problems/valid-boomerang/discuss/286702/JavaC%2B%2BPython-Straight-Forward
        通过斜率(slope)进行判断
        ----------------
        验证通过,性能不错,但是代码有些繁琐:
        Runtime: 32 ms, faster than 91.52% of Python3 online submissions for Valid Boomerang.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Boomerang.
        :param points:
        :return:
        """
        if not points or len(points) != 3 or len(points[0]) != 2:
            return False

        # 重合点过滤
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False

        if points[0][0] - points[1][0] == 0:
            k_1 = 99999999
        else:
            k_1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        if points[2][0] - points[1][0] == 0:
            k_2 = 99999999
        else:
            k_2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        return k_1 != k_2

    def isBoomerang_2(self, points):
        """
        isBoomerang_1()的简化版本,isBoomerang_1主要是考虑了分母为0的情况,通过等式变换可以把除法转换成乘法.
        完全一致的参考思路:
        https://leetcode.com/problems/valid-boomerang/discuss/286702/JavaC%2B%2BPython-Straight-Forward
        :param points:
        :return:
        """
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) != (points[0][0] - points[2][0]) * (
            points[0][1] - points[1][1])

    def isBoomerang_error_1(self, points):
        """
        1.先判断points中是否存在相同的点,如果存在返回False
        2.先根据两点计算出直线公式,再判断第三个点是否在同一条直线上,如果在直线上返回False
        3.返回True
        ------------
        验证失败,无法通过x=0这样的直线
        :param points:
        :return:
        """
        if not points or len(points) != 3 or len(points[0]) != 2:
            return False
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        # y=kx+b
        k = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        b = points[0][1] - k * points[0][0]
        if k * points[2][0] + b == points[2][1]:
            return False
        return True

    def isBoomerang_error_2(self, points):
        """
        1.先判断points中是否存在相同的点,如果存在返回False
        2.利用平行线分线段成比例定理判断三个点是否在同一条直线上,如果在直线上返回False
        3.返回True
        -------
        验证失败,无法验证三个点成等腰三角形的情况,如输入为[[0, 1], [2, 2], [2, 0]]
        :param points:
        :return:
        """
        if not points or len(points) != 3 or len(points[0]) != 2:
            return False
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        # points.sort()
        l1 = (points[0][0] - points[1][0]) * (points[0][0] - points[1][0])
        l2 = (points[0][0] - points[2][0]) * (points[0][0] - points[2][0])
        # 勾股定理
        d1 = l1 + (points[0][1] - points[1][1]) * (points[0][1] - points[1][1])
        d2 = l2 + (points[0][1] - points[2][1]) * (points[0][1] - points[2][1])
        if l1 * d2 == l2 * d1:
            return False
        return True


def main():
    points = [[1, 1], [2, 3], [3, 2]]
    ret = Solution().isBoomerang(points)
    print(ret)
    print("--------------------")

    points = [[1, 1], [2, 2], [3, 3]]
    ret = Solution().isBoomerang(points)
    print(ret)
    print("--------------------")

    points = [[0, 1], [2, 2], [2, 0]]
    ret = Solution().isBoomerang(points)
    print(ret)
    print("--------------------")

    points = [[0, 0], [0, 2], [2, 1]]
    ret = Solution().isBoomerang(points)
    print(ret)
    print("--------------------")

    points = [[0, 0], [1, 1], [1, 1]]
    ret = Solution().isBoomerang(points)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
