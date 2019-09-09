from fractions import Fraction
import math


class Solution:
    """
    https://leetcode.com/problems/fraction-addition-and-subtraction/
    592. Fraction Addition and Subtraction
    medium
    """

    def fractionAddition(self, expression: str) -> str:
        return self.fractionAddition_3(expression)

    def fractionAddition_1(self, expression: str) -> str:
        if expression is None:
            return 0
        numerator1, denominator1 = 0, 1
        numerator2, denominator2 = 0, 1

        # "-1/2+1/2"
        # 1. +，-分割
        # 2. /分割获取分子和分母
        # 3. 根据最小公倍数扩大分母，记录扩大倍数
        # 4. 根据分母的扩大倍数，扩大分子
        # 5. 分子相加或相减
        # 6. 分子，分母简化

        # 处理第一个字符是"-"的情况
        cur_str = expression[0]
        idx = 0
        for s in expression[1:]:
            idx += 1
            if s not in ["+", "-"]:
                cur_str += s
                # 非遍历到最后一个字符时跳出循环
                if idx < len(expression[1:]):
                    continue

            tmp_list = cur_str.split("/")
            numerator2 = int(tmp_list[0])
            denominator2 = int(tmp_list[1])

            # 分数相加或相减
            tmp_d = self.lcm(denominator1, denominator2)
            tmp_n = numerator1 * tmp_d // denominator1 + numerator2 * tmp_d // denominator2

            tmp_gcd = self.gcd(tmp_d, abs(tmp_n))
            if tmp_gcd > 0:
                tmp_n = tmp_n // tmp_gcd
                tmp_d = tmp_d // tmp_gcd
            else:
                tmp_n = 0
                tmp_d = 1

            # numerator1,denominator1存储已经累加的结果
            numerator1, denominator1 = tmp_n, tmp_d
            # print("====", str(numerator1) + "/" + str(denominator1))

            # 重置cur_str
            if s == "-":
                cur_str = "-"
            else:
                cur_str = ""

        return str(numerator1) + "/" + str(denominator1)

    def gcd(self, n1, n2):
        """
        求最大公约数
        """
        l = max(n1, n2)
        s = min(n1, n2)
        t = s
        while t != 0:
            t = l % s
            if t != 0:
                l = s
                s = t
        return s

    def lcm(self, n1, n2):
        """
        最小公倍数
        :param n1:
        :param n2:
        :return:
        """
        return n1 * n2 // self.gcd(n1, n2)

    def fractionAddition_2(self, exp):
        """
        Discuss的解决方案之一
        https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103384/Small-simple-C%2B%2BJavaPython
        :param exp:
        :return:
        """
        res = sum(map(Fraction, exp.replace('+', ' +').replace('-', ' -').split()))
        return str(res.numerator) + '/' + str(res.denominator)

    def fractionAddition_3(self, exp):
        """
        跟简洁的,容易理解的方法
        :param exp:
        :return:
        """
        if exp is None:
            return ""

        exp_arr = exp.replace("+", " +").replace("-", " -").split()
        n1, d1 = 0, 1
        for frac in exp_arr:
            if frac:
                n2 = int(frac.split("/")[0])
                d2 = int(frac.split("/")[1])
                n1 = n1 * d2 + n2 * d1
                d1 = d1 * d2
                gcd = math.gcd(abs(n1), abs(d1))
                n1 = n1 // gcd
                d1 = d1 // gcd
        return "%d/%d" % (n1, d1)


def main():
    a = "-1/2+1/2"
    print("a=", a)
    ret = Solution().fractionAddition(a)
    print(ret)
    print("-----------------")

    a = "-1/2+1/2+1/3"
    print("a=", a)
    ret = Solution().fractionAddition(a)
    print(ret)
    print("-----------------")

    a = "1/3-1/2"
    print("a=", a)
    ret = Solution().fractionAddition(a)
    print(ret)
    print("-----------------")

    a = "5/3+1/3"
    print("a=", a)
    ret = Solution().fractionAddition(a)
    print(ret)
    print("-----------------")

    # n1, n2 = 9, 3
    # ret = Solution().gcd(n1, n2)
    # print(ret)
    # print("-----------------")


if __name__ == "__main__":
    main()
