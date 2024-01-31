"""
65. Valid Number
Hard
----------------------
A valid number can be split up into these components (in order):
    1.A decimal number or an integer.
    2.(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    1.(Optional) A sign character (either '+' or '-').
    2.One of the following formats:
        1.One or more digits, followed by a dot '.'.
        2.One or more digits, followed by a dot '.', followed by one or more digits.
        3.A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
    1.(Optional) A sign character (either '+' or '-').
    2.One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        return self.isNumber_1(s)

    def isNumber_1(self, s: str) -> bool:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：
        1. 分段计算。
        1.1. 根据第一个e或E分段。
        1.1.1. 如果分为1段。判断是否是decimal或integer
        1.1.2. 如果分为2段。第一段是否decimal或integer，第二段是否integer。
        1.1.3. 如果大于等于3段。不是有效number

        另一种解法:
        https://leetcode.com/problems/valid-number/solutions/173977/python-with-simple-explanation/

        Runtime 41 ms Beats 52.50%
        Memory 16.68 MB Beats 58.11%

        Args:
            s:

        Returns:

        """
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        sign = {'+', '-'}

        def isInteger(s: str) -> bool:

            if len(s) <= 0:
                return False
            i = 0
            if s[0] in sign:
                i += 1
            # 注意s=='+'或'-'的情况
            return len(s[i:]) > 0 and len(list(set(s[i:]) - digits)) == 0

        def isDecimal(s: str) -> bool:
            """
            1.(Optional) A sign character (either '+' or '-').
            2.One of the following formats:
                1.One or more digits, followed by a dot '.'.
                2.One or more digits, followed by a dot '.', followed by one or more digits.
                3.A dot '.', followed by one or more digits.
            """
            # 过滤 s=='.'的个情况
            if len(s) <= 0:
                return False

            i = 0
            if s[0] in sign:
                i += 1
            # 过滤 '.'
            if s[i:] == '.':
                return False
            # 根据'.'切割
            arr = s[i:].split('.')
            if len(arr) == 2:
                return len(list(set(arr[0]) - digits)) == 0 and len(list(set(arr[1]) - digits)) == 0
            else:
                return False

        # 根据e或E分割
        nums = s.upper().split('E')
        if len(nums) == 1:
            return isDecimal(nums[0]) or isInteger(nums[0])
        elif len(nums) == 2:
            return (isDecimal(nums[0]) or isInteger(nums[0])) and isInteger(nums[1])
        else:
            return False


def do_func(s: str, expect: list):
    ret = Solution().isNumber(s)
    print("s =", s)
    # print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func("0", True)
    do_func('e', False)
    do_func(".", False)
    do_func("+0", True)
    do_func("-0", True)
    do_func("0000000", True)
    do_func("-0.1", True)
    do_func("-0.000", True)
    do_func("-4.", True)
    do_func("4E+", False)
    do_func("+", False)
    do_func("+-", False)
    do_func("+.-", False)
    do_func("+.", False)
    do_func("+..", False)
    do_func("....", False)
    do_func("+4.", True)

    l1 = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for s in l1:
        do_func(s, False)

    do_func("2e10", True)
    do_func("2E10", True)

    l2 = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for s in l2:
        do_func(s, True)


if __name__ == "__main__":
    main()
