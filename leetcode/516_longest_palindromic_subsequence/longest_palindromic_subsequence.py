"""
https://leetcode.com/problems/longest-palindromic-subsequence/
516. Longest Palindromic Subsequence
Medium
----------------------
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s):
        return self.longestPalindromeSubseq_2(s)

    def longestPalindromeSubseq_2(self, s):
        """
        同样参考
        https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
        只不过遍历方式是从最小面的行开始遍历,每行从左向右遍历
        与longestPalindromeSubseq_1的以对角线为基准遍历不同
        :param s:
        :return:
        """
        if not s:
            return 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(dp) - 1]

    def longestPalindromeSubseq_1(self, s):
        """
        dp问题,参考思路https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
        状态转换公式如下:
        如果 s.charAt(i) == s.charAt(j),dp[i][j] = dp[i+1][j-1] + 2
        否则, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
        初始: dp[i][i] = 1
        ---------------
        验证通过,性能一般
        Runtime: 1908 ms, faster than 38.32% of Python3 online submissions for Longest Palindromic Subsequence.
        Memory Usage: 31.4 MB, less than 51.66% of Python3 online submissions for Longest Palindromic Subsequence.
        :param s:
        :return:
        """
        if not s:
            return 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(dp)):
            dp[i][i] = 1

        # 沿对角线进行遍历,以对角线为基准进行遍历,逐渐遍历到右上dp节点
        for i in range(len(dp) - 1):
            row = 0
            col = i + 1
            for j in range(i + 1, len(dp)):
                if s[row] == s[col]:
                    dp[row][col] = dp[row + 1][col - 1] + 2
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col - 1])
                row += 1
                col += 1
        # print(dp)
        return dp[0][len(dp) - 1]


def main():
    s = "bbbab"
    ret = Solution().longestPalindromeSubseq(s)
    print(ret)
    print(ret == 4)
    print("---------------------")

    s = "cbbd"
    ret = Solution().longestPalindromeSubseq(s)
    print(ret)
    print(ret == 2)
    print("---------------------")


if __name__ == "__main__":
    main()
