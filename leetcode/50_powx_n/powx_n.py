"""
https://leetcode.com/problems/powx-n/
50. Pow(x, n)
Medium
------------
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution:
    def myPow(self, x, n):
        return self.myPow_binary_search_recursive(x, n)

    def myPow_binary_search_iterative(self, x, n):
        """
        思路来源:
        https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        :param x:
        :param n:
        :return:
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

    def myPow_binary_search_recursive_2(self, x, n):
        """
        myPow_binary_search_recursive()的原版解决方案
        https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        :param x:
        :param n:
        :return:
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow_binary_search_recursive_2(x, -n)
        if n % 2:
            return x * self.myPow_binary_search_recursive_2(x, n - 1)
        return self.myPow_binary_search_recursive_2(x * x, n / 2)

    def myPow_binary_search_recursive(self, x, n):
        """
        参考思路:
        https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        验证通过:
        Runtime: 24 ms, faster than 92.32% of Python3 online submissions for Pow(x, n).
        Memory Usage: 13.8 MB, less than 6.90% of Python3 online submissions for Pow(x, n).
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if abs(n) % 2:
            t = self.myPow_binary_search_recursive(x, abs(n) // 2)
            ret = x * t * t
        else:
            t = self.myPow_binary_search_recursive(x, abs(n) // 2)
            ret = t * t
        return ret if n > 0 else 1 / ret

    def myPow_recursive(self, x, n):
        """
        普通递归思路,时间复杂度:O(N)
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        ret = self.myPow_recursive(x, abs(n) // 2) * self.myPow_recursive(x, abs(n) - abs(n) // 2)
        return ret if n > 0 else 1 / ret

    def myPow_iterative(self, x, n):
        """
        验证失败,超时
        Time Complexity: O(n)
        :param x:
        :param n:
        :return:
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        ret = 1
        for i in range(abs(n)):
            ret *= x
        # 下面的代码是多余的,因为"ret *= x"这条代码已经对正负号进行了判断
        # if x < 0:
        #     if n % 2 == 1:
        #         ret *= -1
        if n < 0:
            ret = 1 / ret

        return ret


def main():
    x = 2.00000
    n = 10
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 1024.00000)
    print('--------------------')

    x = 2.10000
    n = 3
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 9.26100)
    print('--------------------')

    x = 2.00000
    n = -2
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 0.25000)
    print('--------------------')

    x = 2.00000
    n = 0
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 1)
    print('--------------------')

    x = 0
    n = 89
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 0)
    print('--------------------')

    x = 2
    n = -3
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == 0.125000)
    print('--------------------')

    x = -2
    n = 3
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == -8)
    print('--------------------')

    x = -2
    n = -3
    ret = Solution().myPow(x, n)
    print(ret)
    print(ret == -0.125)
    print('--------------------')


if __name__ == "__main__":
    main()
