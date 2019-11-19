"""
https://leetcode.com/problems/rectangle-area/
223. Rectangle Area
Medium
-------------------
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:
Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        return self.computeArea_2(A, B, C, D, E, F, G, H)

    def computeArea_1(self, A, B, C, D, E, F, G, H):
        """
        咋一看很简单,但是有坑.需要考虑完全重叠/部分重叠/包含/不重叠等四种情况;还需要注意坐标相减时的大小选择.
        --------------
        验证通过,性能还可以,但是太过于繁琐,耗费了很长时间,调试了很多次,修改了很多次,才得以通过:
        Runtime: 56 ms, faster than 85.27% of Python3 online submissions for Rectangle Area.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rectangle Area.
        :param A:
        :param B:
        :param C:
        :param D:
        :param E:
        :param F:
        :param G:
        :param H:
        :return:
        """
        area1 = abs((C - A) * (D - B))
        area2 = abs((G - E) * (H - F))

        def contain_point(a, b, c, d, p, q):
            """
            前面的矩形是否包含后面的点
            :param a:
            :param b:
            :param c:
            :param d:
            :param p:
            :param q:
            :return:
            """
            if a <= p <= c and b <= q <= d:
                return True
            return False

        # 先对矩形排序,根据left-bottom点的x坐标,保证A,B在最左侧
        if A > E:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D

        # 重点是交叉部分的面积
        if A <= E and B <= F and C >= G and D >= H:  # 完全重叠或完全包含
            area_join = min(area1, area2)
        elif (C <= E) or (D <= F) or (B >= H):  # 不重叠
            area_join = 0
        else:  # 部分重叠
            # p1~p4表示矩形的点的序号,规则:从左下角开始顺时针旋转
            p1 = contain_point(A, B, C, D, E, F)
            p2 = contain_point(A, B, C, D, E, H)
            p3 = contain_point(A, B, C, D, G, H)
            p4 = contain_point(A, B, C, D, G, F)
            if p1 and p2:
                area_join = (C - E) * (H - F)
            elif p1 and p4:
                area_join = (G - E) * (D - F)
            elif p1:
                area_join = (C - E) * (D - F)
            elif p2 and p3:
                area_join = (G - E) * (H - B)
            elif p2:
                area_join = (C - E) * (H - B)
            else:
                # 这里还有两种情况
                if C <= G:  # 第一种情况
                    area_join = (C - E) * (D - B)
                else:  # 第二种情况
                    area_join = (G - E) * (D - B)

        return area1 + area2 - area_join

    def computeArea_2(self, A, B, C, D, E, F, G, H):
        """
        参考思路:
        https://leetcode.com/problems/rectangle-area/discuss/62138/My-Java-solution-Sum-of-areas-Overlapped-area
        :param A:
        :param B:
        :param C:
        :param D:
        :param E:
        :param F:
        :param G:
        :param H:
        :return:
        """
        area1 = abs((C - A) * (D - B))
        area2 = abs((G - E) * (H - F))

        left = max(A, E)
        right = min(C, G)
        bottom = max(B, F)
        top = min(D, H)
        area_join = 0
        if left < right and bottom < top:
            area_join = (right - left) * (top - bottom)
        return area1 + area2 - area_join


def main():
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")

    A = -3
    B = 0
    C = 3
    D = 4
    E = -3
    F = 0
    G = 3
    H = 4
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")

    A = 3
    B = 3
    C = 3
    D = 3
    E = 3
    F = 3
    G = 3
    H = 3
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")

    A = 1
    B = 1
    C = 2
    D = 2
    E = 10
    F = 10
    G = 20
    H = 20
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")

    A = -5
    B = -5
    C = 5
    D = 3
    E = -3
    F = -3
    G = 3
    H = 3
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")

    A = -5
    B = -2
    C = 5
    D = 1
    E = -3
    F = -3
    G = 3
    H = 3
    ret = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
