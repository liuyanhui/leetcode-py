"""
67. Add Binary
Easy
-------------------------------
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.addBinary_1(a, b)

    def addBinary_1(self, a: str, b: str) -> str:
        """
        Round 3
        Score[4] Lower is harder

        Thinking：
        1. binary相加公式为：
        1+1=10
        1+0=1
        0+1=1
        0+0=0
        2. 要注意进位carry存在的情况
        1+1+1=11 (3%2=1 3/2=1)

        验证通过

        Args:
            a:
            b:

        Returns:

        """
        ret = ''
        carry = 0
        i = 0
        len_a, len_b = len(a), len(b)
        while i < len_a or i < len_b:
            t = 0
            if i < len_a:
                t += int(a[len_a - 1 - i])
            if i < len_b:
                t += int(b[len_b - 1 - i])
            t += carry
            ret += str(t % 2)
            carry = t // 2
            i += 1
        if carry > 0:
            ret += str(carry)
        return ret[::-1]


def do_func(a: str, b: str, expect: str):
    ret = Solution().addBinary(a, b)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func("11", "1", "100")
    do_func("1010", "1011", "10101")
    do_func("1", "1", "10")
    do_func("0", "0", "0")
    do_func("11", "0", "11")


if __name__ == "__main__":
    main()
