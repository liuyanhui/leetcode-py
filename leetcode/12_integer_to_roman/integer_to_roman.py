"""
https://leetcode.com/problems/integer-to-roman/
12. Integer to Roman
Medium
-------------------
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
"""


class Solution:
    def intToRoman(self, num):
        return self.intToRoman_3(num)

    def intToRoman_3(self, num):
        """
        参考思路:
        https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
        :param num:
        :return:
        """
        ret = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(values)):
            tmp = num // values[i]
            ret += numerals[i] * tmp
            num = num % values[i]
        return ret

    def intToRoman_2(self, num):
        """
        参考思路:
        https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution
        :param num:
        :return:
        """
        if num <= 0 or num >= 4000:
            return ""
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num // 100) % 10] + X[(num // 10) % 10] + I[num % 10]

    def intToRoman_1(self, num):
        """
        朴素的直接的思路,代码略多
        验证通过:
        Runtime: 44 ms, faster than 80.91% of Python3 online submissions for Integer to Roman.
        Memory Usage: 14.4 MB, less than 16.40% of Python3 online submissions for Integer to Roman.
        :param num:
        :return:
        """
        if num <= 0 or num >= 4000:
            return ""
        ret = ""
        # 千位数
        tmp = num // 1000
        while tmp > 0:
            ret += "M"
            tmp -= 1
        # 百位
        tmp = (num - (num // 1000) * 1000) // 100
        if tmp == 9:
            ret += "CM"
        elif 5 <= tmp <= 8:
            ret += "D"
            tmp -= 5
            while tmp > 0:
                ret += "C"
                tmp -= 1
        elif tmp == 4:
            ret += "CD"
        else:
            while tmp > 0:
                ret += "C"
                tmp -= 1
        # 十位
        tmp = (num - (num // 100) * 100) // 10
        if tmp == 9:
            ret += "XC"
        elif 5 <= tmp <= 8:
            ret += "L"
            tmp -= 5
            while tmp > 0:
                ret += "X"
                tmp -= 1
        elif tmp == 4:
            ret += "XL"
        else:
            while tmp > 0:
                ret += "X"
                tmp -= 1
        # 个位
        tmp = num - (num // 10) * 10
        if tmp == 9:
            ret += "IX"
        elif 5 <= tmp <= 8:
            ret += "V"
            tmp -= 5
            while tmp > 0:
                ret += "I"
                tmp -= 1
        elif tmp == 4:
            ret += "IV"
        else:
            while tmp > 0:
                ret += "I"
                tmp -= 1

        return ret


def main():
    num = 3
    ret = Solution().intToRoman(num)
    print(ret)
    print(ret == "III")
    print("---------------------")

    num = 4
    ret = Solution().intToRoman(num)
    print(ret)
    print(ret == "IV")
    print("---------------------")

    num = 9
    ret = Solution().intToRoman(num)
    print(ret)
    print(ret == "IX")
    print("---------------------")

    num = 58
    ret = Solution().intToRoman(num)
    print(ret)
    print(ret == "LVIII")
    print("---------------------")

    num = 1994
    ret = Solution().intToRoman(num)
    print(ret)
    print(ret == "MCMXCIV")
    print("---------------------")


if __name__ == "__main__":
    main()
