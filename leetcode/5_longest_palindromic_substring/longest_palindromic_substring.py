"""
https://leetcode.com/problems/longest-palindromic-substring/
5. Longest Palindromic Substring
Medium
----------------------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longestPalindrome(self, s):
        """
        Time complexity:O(N*N)
        Spave complexity:O(N)
        验证通过,性能不错
        Runtime: 728 ms, faster than 91.18% of Python3 online submissions for Longest Palindromic Substring.
        Memory Usage: 14.1 MB, less than 76.49% of Python3 online submissions for Longest Palindromic Substring.
        :param s:
        :return:
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        ret = ""
        for i in range(len(s)):
            l = r = i
            while r < len(s) and s[l] == s[r]:
                r += 1
            if len(ret) < r - l:
                ret = s[l:r]
            # 查找中间相同字符后,l向左移动一位
            l -= 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(ret) < r - l - 1:
                ret = s[l + 1:r]

        return ret

    def longestPalindrome_error1(self, s):
        """
        思路比较简单,依次向右遍历.共有两种情况:1.右边的和第i个相等,那么继续向右遍历;2.左边和右边的相等,继续向左右遍历
        这种无法解决输入是"abccba"的用例,即无法解决中间部分是相同字符的用例.
        :param s:
        :return:
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        ret = ""
        for i in range(len(s)):
            l = r = i
            while r < len(s) and s[i] == s[r]:
                r += 1
            if len(ret) < r - i:
                ret = s[i:r]
            # 错误的问题出在这里,先查找完相等的子串后,应该从该子串的左右开始进行查找.假设子串为[l,r],应该从l-1向左,r+1向右开始查找
            # 正确应该是把下面的一行代码改成l-=1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(ret) < r - l - 1:
                ret = s[l + 1:r]

        return ret


def main():
    s = "babad"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "bab")
    print("---------------------")

    s = "cbbd"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "bb")
    print("---------------------")

    s = "a"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "a")
    print("---------------------")

    s = "ac"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "a")
    print("---------------------")

    s = "aaaaaaaaaaaaa"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "aaaaaaaaaaaaa")
    print("---------------------")

    s = "zxcvbnmmnbvcxz"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "zxcvbnmmnbvcxz")
    print("---------------------")

    s = "abccba"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "abccba")
    print("---------------------")

    s = "abcba"
    ret = Solution().longestPalindrome(s)
    print(ret)
    print(ret == "abcba")
    print("---------------------")


if __name__ == "__main__":
    main()
