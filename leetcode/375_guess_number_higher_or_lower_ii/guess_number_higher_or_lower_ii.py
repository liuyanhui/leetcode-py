"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/
375. Guess Number Higher or Lower II
Medium
--------------------
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:
n = 10, I pick 8.
First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.
Game over. 8 is the number I picked.
You end up paying $5 + $7 + $9 = $21.

Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""


class Solution:
    def getMoneyAmount(self, n):
        return self.getMoneyAmount_loop(n)

    def getMoneyAmount_recursive(self, n):
        """
        Minimax算法+DP,递归法
        参考思路:
        https://www.cnblogs.com/grandyang/p/5677550.html
        https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84766/Clarification-on-the-problem-description.-Problem-description-need-to-be-updated-!!!
        总结推导公式为:
        dp[i][j] = min(k + max(dp[i][k-1],dp[k+1][j])),其中dp[i][j]为从i到j的最优解,i<=k<=j
        1.当只有一个数时,返回0.即,dp[i][i]=0
        2.当有两个连续的数时,返回最小值.即,dp[m][n]=m,其中m+1=n
        3.当有三个连续的数时,返回中间值.即.dp[m][n]=(m+n)/2,其中m+2=n
        返回dp[1][n]
        ----------------
        验证通过,性能一般
        Runtime: 1260 ms, faster than 24.52% of Python3 online submissions for Guess Number Higher or Lower II.
        Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        def do_dp(i, j):
            if i >= j:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            tmp = 99999999
            for k in range(i, j + 1):
                tmp = min(tmp, k + max(do_dp(i, k - 1), do_dp(k + 1, j)))
            dp[i][j] = tmp
            return dp[i][j]

        do_dp(1, n)
        return dp[1][n]

    def getMoneyAmount_loop(self, n):
        """
        Minimax算法+DP,循环法
        参考:https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84764/Simple-DP-solution-with-explanation~~
        推导公式:dp[i][j] = min(k + max(dp[i][k-1],dp[k+1][j])),其中dp[i][j]为从i到j的最优解,i<=k<=j
        思路解释:
        由于计算dp矩阵需要用到前序计算的结果,所以循环方式的选择很关键.
        -------------
        验证通过,性能中等
        Runtime: 708 ms, faster than 54.69% of Python3 online submissions for Guess Number Higher or Lower II.
        Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.
        :param self:
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        dp = [[0 for i in range(n + 2)] for j in range(n + 2)]
        for j in range(1, n + 1):
            for i in range(j - 1, 0, -1):
                tmp = 999999
                for k in range(i, j + 1):
                    # 需要防止数据index溢出
                    tmp = min(tmp, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = tmp
        return dp[1][n]


def main():
    n = 10
    ret = Solution().getMoneyAmount(n)
    print(ret)
    print(ret == 16)
    print("--------------------")

    n = 20
    ret = Solution().getMoneyAmount(n)
    print(ret)
    print(ret == 49)
    print("--------------------")

    n = 1
    ret = Solution().getMoneyAmount(n)
    print(ret)
    print("--------------------")

    n = 2
    ret = Solution().getMoneyAmount(n)
    print(ret)
    print("--------------------")

    n = 3
    ret = Solution().getMoneyAmount(n)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
