"""
https://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings. You may assume that all characters in both strings are different
Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB
An interleaved string of given two strings preserves the order of characters in individual strings. For example, in all the interleavings of above first example, ‘A’ comes before ‘B’ and ‘C’ comes before ‘D’.
----------------
leetcode 类似的题目
https://leetcode.com/problems/interleaving-string/
97. Interleaving String
Hard
"""


class Solution:
    def generate_all_interleavings(self, a, b):
        return self.generate_all_interleavings_1(a, b)

    def generate_all_interleavings_1(self, a, b):
        """
        参考思路:
        https://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
        个人解析:
        1.结果集元素数量计算公式,如下:
            count(m, n) = count(m-1, n) + count(m, n-1)
            count(1, 0) = 1 and count(0, 1) = 1
        2.上面的公式虽然是数量计算公式,但是放在结果集生成也是可行的,将上面的递归公式可以转换成二叉树的显示方式,更加直观.
        3.根据二叉树可以写出相应的代码实现
        -----------
        其中,step1和step2非常关键
        :param a:
        :param b:
        :return:
        """
        if not a:
            return b
        if not b:
            return a
        ret = []
        recusive_rs = []

        def real_generate(str1, str2, tmp_rs, m, n):
            if not m and not n:
                ret.append("".join(tmp_rs))

            if m > 0:
                tmp_rs.append(str1[0])
                real_generate(str1[1:], str2, tmp_rs, m - 1, n)
                tmp_rs.pop()

            if n > 0:
                tmp_rs.append(str2[0])
                real_generate(str1, str2[1:], tmp_rs, m, n - 1)
                tmp_rs.pop()

        real_generate(a, b, recusive_rs, len(a), len(b))
        return ret


def main():
    a = "AB"
    b = ""
    ret = Solution().generate_all_interleavings(a, b)
    print(ret)
    print("--------------------------")

    a = "AB"
    b = "CD"
    ret = Solution().generate_all_interleavings(a, b)
    print(ret)
    print("--------------------------")

    a = "AB"
    b = "C"
    ret = Solution().generate_all_interleavings(a, b)
    print(ret)
    print("--------------------------")

    a = "AC"
    b = "AC"
    ret = Solution().generate_all_interleavings(a, b)
    print(ret)
    print("--------------------------")


if __name__ == "__main__":
    main()
