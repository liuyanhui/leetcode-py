class Solution:
    """
    https://leetcode.com/problems/solve-the-equation/
    640. Solve the Equation
    Medium
    """
    def solveEquation(self, equation):
        return self.solveEquation_1(equation)

    def solveEquation_1(self, equation):
        """
        1.输入字符种类：字母x、数字、加号、减号、等号
        2.输入等式合并：x等式左边，数字等式右边
        3.合并后结果三种情况：0=0;x=?;?=0
        """
        if equation is None or len(equation.lstrip().rstrip()) <= 2:
            return "No solution"

        # 存字母数量，等式左边
        left = 0
        # 存数字之和，等式右边
        right = 0
        # 存等号数量
        mid = 1
        cur_str = ""

        for s in equation:
            # 遇到+，-，=时，开始进行逻辑处理
            if s in ["+", "-", "="]:
                if len(cur_str) == 0:
                    cur_str = s
                    continue
                # print(cur_str)
                if cur_str == "x":
                    left += mid * 1
                elif cur_str == "-x":
                    left += mid * -1
                elif cur_str.find("x") > 0:
                    # 去掉x，并入left
                    left += mid * int(cur_str[0:-1])
                else:
                    # 并入right
                    right += -1 * mid * int(cur_str)

                cur_str = ""
                # +,—,=符号的处理
                if s == "=":
                    mid = -1
                    # print("left=%d,right=%d" % (left, right))
                elif s == "-":
                    cur_str = s
            else:
                cur_str += s

        # 循环结束后剩余字符的处理
        if len(cur_str) > 0:
            if cur_str == "x":
                left += mid * 1
            elif cur_str == "-x":
                left += mid * -1
            elif cur_str.find("x") > 0:
                # 去掉x，并入left
                left += mid * int(cur_str[0:-1])
            else:
                # 并入right
                right += -1 * mid * int(cur_str)

        # print("left=%d,right=%d" % (left, right))
        # 合并的结果只有三种情况：0=0;x=?;?=0;0=?
        if left == 0 and right == 0:
            return "Infinite solutions"
        elif left != 0 and right == 0:
            return "x=0"
        elif left == 0 and right != 0:
            return "No solution"
        else:
            return "x=" + str(right // left)

    def solveEquation_2(self, equation):
        z = eval(equation.replace('x', 'j').replace('=', '-(') + ')', {'j': 1j})
        # print(equation.replace('x', 'j').replace('=', '-(') + ')')
        # print(z)
        a, x = z.real, -z.imag
        # print("a=%d,x=%d" % (a, x))
        return 'x=%d' % (a / x) if x else 'No solution' if a else 'Infinite solutions'


def main():
    a = "x+5-3+x=6+x-2"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")

    a = "x=x"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")

    a = "2x=x"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")

    a = "2x+3x-6x=x+2"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")

    a = "x=x+2"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")

    a = "-x+x+3x=2x-x+x"
    print("a =", a)
    ret = Solution().solveEquation(a)
    print("ret =", ret)
    print("--------------")


if __name__ == "__main__":
    main()
