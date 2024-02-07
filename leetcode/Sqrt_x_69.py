"""
69. Sqrt(x)
Easy
-----------------------------
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.mySqrt_3(x)

    def mySqrt_3(self, x: int) -> int:
        """
        Round 3
        Score[2] Lower is harder

        比mySqrt_2()更好理解的binary search方法
        https://leetcode.com/problems/sqrtx/solutions/25047/a-binary-search-solution/

        验证通过:

        """
        if x == 0: return 0
        l, r = 1, x // 2
        while l <= r:
            mid = r - (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                l = mid + 1
        return l

    def mySqrt_2(self, x: int) -> int:
        """
        Round 3
        Score[2] Lower is harder

        二分查找法,
        参考:
        1. java版round2
        2. https://leetcode.com/problems/sqrtx/solutions/25047/a-binary-search-solution/

        验证通过:
        Runtime 30 ms Beats 96.34%
        Memory 16.67 MB Beats 53.60%
        """
        if x == 0: return 0
        if x == 1: return 1

        l, r = 1, x // 2  # review l=0时,x=2和x=3无法通过,存在mid=0的情况
        while l <= r:
            mid = (r + l) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                l = mid + 1
            else:
                r = mid - 1
        return r  # review 这是二分查找中少有的返回right的题目，一般来说都是返回left

    def mySqrt_1(self, x: int) -> int:
        """
        验证通过:
        性能较差.
        可以在i的步进方面进行改善;或使用二分查找法.

        """
        i = 0
        while (i + 1) * (i + 1) <= x:
            i += 1
        return i


def do_func(x: int, expect: int):
    ret = Solution().mySqrt(x)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(4, 2)
    do_func(8, 2)
    do_func(0, 0)
    do_func(1, 1)
    do_func(2 ** 32 - 1, 65535)
    do_func(24, 4);
    do_func(1600000000, 40000);
    do_func(2147483647, 46340);
    do_func(2147395599, 46339);
    do_func(5, 2)
    do_func(3, 1)
    do_func(2, 1)
    do_func(36, 6)


if __name__ == "__main__":
    main()
