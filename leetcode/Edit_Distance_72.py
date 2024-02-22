"""
72. Edit Distance
Medium
-------------------------------
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
 - Insert a character
 - Delete a character
 - Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance_1(word1, word2)

    def minDistance_1(self, word1: str, word2: str) -> int:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：
        1. naive solution 穷举法
        每个字母都有三种操作方式，遍历+递归+穷举。
        字母相同时，不做操作；字母不同时，穷举三种操作；word1到结尾时，insert；word2到结尾时，delete。
        时间复杂度：O(3^N)
        2. 递归可以转化为DP。
        前提：
        m=len(word1),n=len(word2)
        dp[m+1][n+1]
        dp[0][:]=[0,1...,n]
        dp[:][0]=[0,1...,n]
        dp[i][j]为word1[0:i+1]和word2[0:j+1]的最优解
        算法为：
        遍历word1和word2，按行遍历
        IF word1[i]==word2[j] THEN dp[i][j]=dp[i-1][j-1]
        IF word1[i]!=word2[j] THEN min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

        验证通过:
        Runtime 105 ms Beats 54.86%
        Memory 20.18 MB Beats 54.36%
        """
        m, n = len(word1), len(word2)
        # 初始化dp
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 第0列初始化,相当于空字符''和字符串word1[0:i]进行转换
        for i in range(m + 1):
            dp[i][0] = i
        # 第0行初始化,相当于空字符''和字符串word2[0:j]进行转换
        for j in range(n + 1):
            dp[0][j] = j
        # 遍历并计算dp
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # review dp[i][j]对应replace; dp[i + 1][j]对应insert; dp[i][j + 1]对应delete
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1

        return dp[m][n]


def do_func(word1: str, word2: str, expect: int):
    ret = Solution().minDistance(word1, word2)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func("horse", "ros", 3)
    do_func("intention", "execution", 5)
    do_func("", "", 0);
    do_func("horse", "", 5);
    do_func("", "ros", 3);
    do_func("qwertyuio", "asdfghjkl", 9);
    do_func("abcdef", "efghij", 6);
    do_func("abcdef", "xyzab", 6);
    do_func("abc", "abc", 0);


if __name__ == "__main__":
    main()
