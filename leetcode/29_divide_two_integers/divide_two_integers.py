"""
https://leetcode.com/problems/divide-two-integers/
29. Divide Two Integers
Medium
---------------------
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""
import sys


class Solution:
    def divide(self, dividend, divisor):
        """
        不能用乘\除\mod操作,我们可以通过左移位<<2来模拟乘以2的情况.
        思路如下:
        1.我们通过循环可以计算出divisor*(2^n)<dividend<divisor*(2^(n+1)).
        2.那么商必然在2^n和2^(n+1)之间,
        3.然后递归执行步骤1,每次递归的结果2^n相加即可
        4.需要考虑边界值等特殊情况,如:最大整数,最小整数,除数为1的情况.
        5.需要考虑负数.
        举例说明:
        1.如10/3时,有3*(2^1)<10<3*(2^2),那么商必然落在2^1~2^2之间.记录2^1=2
        2.递归步骤1.此时输入为:(10-3*2*1)/3,即4/3,有3*(2^0)<4<3*(2^1).记录2^0=1
        3.最终结果为2^1+2^0=2+1=3
        ------------------
        验证通过:
        Runtime: 36 ms, faster than 35.24% of Python3 online submissions for Divide Two Integers.
        Memory Usage: 14 MB, less than 7.41% of Python3 online submissions for Divide Two Integers.
        :param dividend:
        :param divisor:
        :return:
        """
        if divisor == 0 or dividend == 0:
            return 0

        if divisor==1:
            return dividend

        if divisor == -1:
            # 只要不是最小的那个整数，都是直接返回相反数就好啦
            if dividend > -2147483648:
                return -dividend
            # 是最小的那个，那就返回最大的整数啦
            return 2147483647

        def divide_rescursive(d1, d2):
            if d1 < d2 or (d1 + d2) < max(d1, d2):
                return 0

            d21, d22 = 0, d2
            i = 0
            ret = 0
            while d1 >= d22:
                d21 = d22
                i += 1
                d22 <<= 1
            ret += 1 << (i - 1)
            ret += divide_rescursive(d1 - d21, d2)
            return ret

        trun = divide_rescursive(abs(dividend), abs(divisor))
        if min(dividend, divisor) < (dividend + divisor) < max(dividend, divisor):
            trun = -trun

        return trun


def main():
    dividend = 10
    divisor = 3
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 3)
    print('--------------------')

    dividend = -10
    divisor = 3
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == -3)
    print('--------------------')

    dividend = 3
    divisor = 3
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 1)
    print('--------------------')

    dividend = -2147483648
    divisor = -1
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 2147483647)
    print('--------------------')

    dividend = 2147483647
    divisor = 1
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 2147483647)
    print('--------------------')

    dividend = 2147483647
    divisor = 2
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 1073741823)
    print('--------------------')

    dividend = 160
    divisor = 2
    ret = Solution().divide(dividend, divisor)
    print(ret)
    print(ret == 80)
    print('--------------------')


if __name__ == "__main__":
    main()
