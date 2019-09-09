"""
https://leetcode.com/problems/implement-strstr/
28. Implement strStr()
Easy
-----------------------------------
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        return self.strStr_3(haystack, needle)

    def strStr_1(self, haystack, needle):
        """
        常规方法
        :param haystack:
        :param needle:
        :return:
        """
        if haystack is None:
            return -1
        if needle is None or len(needle.strip()) == 0:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr_2(self, haystack, needle):
        """
        另一种实现方法
        :param haystack:
        :param needle:
        :return:
        """
        if haystack is None:
            return -1
        if needle is None or len(needle.strip()) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    count += 1
                else:
                    count = 0
                    break
            if count == len(needle):
                return i
        return -1

    def strStr_3(self, haystack, needle):
        """
        另一种实现方法
        :param haystack:
        :param needle:
        :return:
        """
        if haystack is None:
            return -1
        if needle is None or len(needle.strip()) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                else:
                    break
        return -1


def main():
    haystack = "hello"
    needle = "ll"
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = "aaaaa"
    needle = "bba"
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = "sdsd"
    needle = ""
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = ""
    needle = ""
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = "aaa"
    needle = "aaaa"
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = "mississippi"
    needle = "sipp"
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")

    haystack = "a"
    needle = "a"
    ret = Solution().strStr(haystack, needle)
    print(ret)
    print("------------")


if __name__ == '__main__':
    main()
