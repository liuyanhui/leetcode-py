"""
https://leetcode.com/problems/largest-triangle-area/
812. Largest Triangle Area
Easy
----------------
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.

Notes:
3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""


class Solution:
    def largestTriangleArea(self, points):
        return self.largestTriangleArea_3(points)

    def largestTriangleArea_3(self, points):
        """
        采用shoelace公式计算三角形面积
        参考文档:
        https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove
        https://blog.csdn.net/stereohomology/article/details/46942889
        公式为:
        S=1/2∣((x1×y2)+(x2×y3)+(x3×y1))−((y1×x2)+(y2×x3)+(y3×x1))∣
        --------
        验证通过
        :param points:
        :return:
        """
        if not points:
            return 0
        max_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    tmp_area = abs(
                                   points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][
                                       1] -
                                   points[j][0] * points[i][1] - points[k][0] * points[j][1] - points[i][0] * points[k][
                                       1]) / 2
                    max_area = max(max_area, tmp_area)
        return max_area

    def largestTriangleArea_2(self, points):
        """
        0.遍历所有点,获取其中的三个点
        1.判断是否三角形
        2.计算出三角形的外接长方形的顶点(至少有三角形的一个顶点和正方形的顶点重合,至多有两个重合的顶点),为max_x,max_y,min_x,min_y
        3.计算出三角形和外接长方形的空隙的面积,至多存在三块空隙三角形(6个线段).依次计算长方形4个顶点和三角形两个顶点的面积.
        4.长方形面积减去空隙面积记为三角形面积
        5.通过三角形面积计算得到最大面积
        ------------
        验证失败,求三角形面试失败用例[2, 5] [10, 10] [1, 1],这个三角形并不是三个顶点都在长方形的边上,有个顶点落在正方形内部
        :param points:
        :return:
        """
        if not points:
            return 0
        max_area = 0

        def is_triangle(p1, p2, p3):
            """计算是否为撒娇性"""
            return (p2[1] - p1[1]) * (p3[0] - p1[0]) != (p3[1] - p1[1]) * (p2[0] - p1[0])

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    # 判断是否为三角形
                    if is_triangle(points[i], points[j], points[k]):
                        # 计算出三角形的外接长方形的顶点
                        max_x = max(points[i][0], points[j][0], points[k][0])
                        max_y = max(points[i][1], points[j][1], points[k][1])
                        min_x = min(points[i][0], points[j][0], points[k][0])
                        min_y = min(points[i][1], points[j][1], points[k][1])
                        rect_area = (max_x - min_x) * (max_y - min_y)
                        # 依次计算长方形4个顶点和三角形两个顶点的面积.
                        # 选择三角形的两个顶点,计算空隙面积
                        l_x = abs(points[i][0] - points[j][0])
                        l_y = abs(points[i][1] - points[j][1])
                        area1 = l_x * l_y / 2
                        l_x = abs(points[i][0] - points[k][0])
                        l_y = abs(points[i][1] - points[k][1])
                        area2 = l_x * l_y / 2
                        l_x = abs(points[j][0] - points[k][0])
                        l_y = abs(points[j][1] - points[k][1])
                        area3 = l_x * l_y / 2
                        print(points[i], points[j], points[k])
                        print(rect_area - area1 - area2 - area3)
                        print("===============")
                        max_area = max(rect_area - area1 - area2 - area3, max_area)

        return max_area

    def largestTriangleArea_1(self, points):
        """
        1.任选三个点A,B,C
        2.判断是否可以组成三角形
        3.计算A,B的长度|AB|,计算A,B的直线公式得出k1和b1
        4.计算直线AB的垂直的直线公式CD,得出k2和b2
        5.CD和AB必然相交,求出焦点D,并结算CD长度|CD|
        6.area=|AB|*|CD|/2
        ----------
        这个方法太笨,太复杂,不适合
        :param points:
        :return:
        """
        if not points:
            return 0

        def calc_distance(p1, p2):
            """计算两点间的长度"""
            pass

        def calc_slope(p1, p2):
            """计算两点间的直线斜率"""
            pass

        def calc_intercept(p1, p2):
            """计算两点间直线公式的截距"""
            pass

        def calc_area(p1, p2, p3):
            """计算三角形的面积"""
            d12 = calc_distance(p1, p2)  # 计算两点长度
            slope_vertical = -1 / slope1  # 计算垂线斜率
            itercept_vertical = points[k][1] - slope_vertical * points[k][0]  # 计算垂线截距
            j_x = ()

        max_area = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    slope1 = calc_slope(points[i], points[j])
                    slope2 = calc_slope(points[k], points[j])
                    if slope1 != slope2:
                        d12 = calc_distance(points[i], points[j])  # 计算两点长度
                        slope_vertical = -1 / slope1  # 计算垂线斜率
                        itercept_vertical = points[k][1] - slope_vertical * points[k][0]  # 计算垂线截距
                        # TODO 过于复杂,不适合

        return max_area


def main():
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    ret = Solution().largestTriangleArea(points)
    print(ret)
    print("--------------------")

    points = [[2, 5], [7, 7], [10, 8], [10, 10], [1, 1]]
    ret = Solution().largestTriangleArea(points)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
