"""
https://leetcode.com/problems/can-i-win/
464. Can I Win
Medium
-------------------------
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.
You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example
Input:
maxChoosableInteger = 10
desiredTotal = 11
Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""
import collections


class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        本质上还是dp问题
        :param maxChoosableInteger:
        :param desiredTotal:
        :return:
        """
        return self.canIWin_2(maxChoosableInteger, desiredTotal)

    def canIWin_1(self, maxChoosableInteger, desiredTotal):
        """
        参考思路:
        https://leetcode.com/problems/can-i-win/discuss/95277/Java-solution-using-HashMap-with-detailed-explanation
        部分核心判断思路可以参考canIWin_error_1()
        ---------------
        验证通过,性能一般
        Runtime: 1584 ms, faster than 5.04% of Python3 online submissions for Can I Win.
        Memory Usage: 29.3 MB, less than 100.00% of Python3 online submissions for Can I Win.
        :param maxChoosableInteger:
        :param desiredTotal:
        :return:
        """
        if sum(list(range(maxChoosableInteger + 1))) < desiredTotal:
            return False
        if maxChoosableInteger >= desiredTotal:
            return True
        used = [False for i in range(maxChoosableInteger + 1)]
        cache = collections.defaultdict(int)  # 0:未计算;1:True;-1:False

        def helper(d):
            if d <= 0: return False
            key = format(used)
            if cache[key] == 0:
                for i in range(1, maxChoosableInteger + 1):
                    if not used[i]:
                        used[i] = True
                        if not helper(d - i):
                            cache[key] = 1
                            used[i] = False
                            return True
                        used[i] = False
                cache[key] = -1
            return cache[key] == 1

        def format(list_used):
            # return str(list_used)
            f_ret = 0
            for n in list_used:
                f_ret <<= 1
                if n:
                    f_ret += 1
            return f_ret

        ret = helper(desiredTotal)
        return ret

    def canIWin_2(self, maxChoosableInteger, desiredTotal):
        """
        参考思路:
        https://leetcode.com/problems/can-i-win/discuss/95292/Python-solution-easy-to-understand
        :param maxChoosableInteger:
        :param desiredTotal:
        :return:
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger < desiredTotal:
            return False

        def helper(arr, d):
            if d <= 0:
                return False
            key = str(arr)
            if key in cache:
                return cache[key]

            if arr[-1] > d:  # if the largest choice exceeds the remainder, then we can win!
                return True

            for i in range(len(arr)):
                if not helper(arr[:i] + arr[i + 1:], d - arr[i]):
                    cache[key] = True
                    return True
            cache[key] = False
            return cache[key]

        cache = {}

        return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

    def canIWin_error_1(self, maxChoosableInteger, desiredTotal):
        """
        dynamic plan 问题,公式如下:
        f(m,d)=!f(m,d-1) or !f(m,d-2) or !f(m,d-3) or .... or f(m,d-m)
        转化为:
        f(m,d)=!f(m,d-m) or !f(m,d-m+1) or !f(m,d-m+2) or .... or f(m,d)
        其中
        f(m,1)=True
        思路描述:
        1.m和d两个变量中,在解题过程中m是固定的,因为变化的m对问题的解决没有任何帮忙,反而会无限扩大解空间,增加难度.
        2.在dp推导工程中,m是固定的,通过增加或者减少d进行计算
        3.player1是否能win,取决于m确定的情况下,d-1到d-m的情况中,player2是否存在至少一种必输的情况;如果player2 在d-1到d-m时存在必输的情况,在下一步player1只需取走<=m的数字就会win.
          换句话说:如果player1 win那么,player2在d-1到d-m的m中情况中必然存在至少一种lose的情况.
        4.f(m,d)是无状态的,它不关心到底是player1还是player2.
        5.f(m,d)=dp[d].dp[d]=!dp[d-1] or !dp[d-2] or ... or !dp[d-m]
        ----------------
        验证失败,没有考虑maxChoosableInteger中的数字不能重复出现.
        如果去掉这个条件,这个实现就是正确的.
        :param maxChoosableInteger:
        :param desiredTotal:
        :return:
        """
        if maxChoosableInteger >= desiredTotal:
            return True
        dp = [False for i in range(desiredTotal + 1)]
        for i in range(1, desiredTotal + 1):
            if i <= maxChoosableInteger:
                dp[i] = True
                continue
            for j in range(1, maxChoosableInteger + 1):
                if not dp[i - j]:
                    dp[i] = True
                    break
        return dp[desiredTotal]


def main():
    # m = 10
    # d = 11
    # ret = Solution().canIWin(m, d)
    # print(ret)
    # print("--------------------")

    m = 10
    d = 12
    ret = Solution().canIWin(m, d)
    print(ret)
    print("--------------------")

    m = 1
    d = 11
    ret = Solution().canIWin(m, d)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
