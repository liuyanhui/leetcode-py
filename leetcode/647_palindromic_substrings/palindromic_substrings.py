"""
https://leetcode.com/problems/palindromic-substrings/
647. Palindromic Substrings
Medium
------------------------
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s):
        """
        这个题的思路与"5. Longest Palindromic Substring"是相似的.
        遍历整个字符串,每个字符的处理有三种情况:
        1.自己
        2.只向右查找与当前字符相等的情况,每找到一个累加;如果不相等,退出.
        3.同时向左右查找,如果是回文字符串,累加;如果不相等,退出.
        验证通过,性能不错
        Runtime: 112 ms, faster than 84.01% of Python3 online submissions for Palindromic Substrings.
        Memory Usage: 14.4 MB, less than 36.34% of Python3 online submissions for Palindromic Substrings.
        :param s:
        :return:
        """
        if not s:
            return 0
        ret = 0
        for i in range(len(s)):
            # 计算自己
            ret += 1
            # 只向右,不包含自己
            r = i + 1
            while r < len(s) and s[i] == s[r]:
                ret += 1
                r += 1
            # 同时向左右扩大
            l = i - 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1
        return ret


def main():
    # s = "abc"
    # ret = Solution().countSubstrings(s)
    # print(ret)
    # print(ret == 3)
    # print("---------------------")
    #
    # s = "aaa"
    # ret = Solution().countSubstrings(s)
    # print(ret)
    # print(ret == 6)
    # print("---------------------")

    s = "aba"
    ret = Solution().countSubstrings(s)
    print(ret)
    print(ret == 4)
    print("---------------------")


if __name__ == "__main__":
    main()
