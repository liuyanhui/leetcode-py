"""
https://leetcode.com/problems/predict-the-winner/
486. Predict the Winner
Medium
-----------------------------------
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""
import collections


class Solution:
    def PredictTheWinner(self, nums):
        return self.PredictTheWinner_4(nums)

    def PredictTheWinner_4(self, nums):
        """
        PredictTheWinner_3()的优化版本,思路如下:
        从推导公式dp[i][j] = max(sum-dp[i+1][j],sum-dp[i][j-1])可以得出,二维数组是多余的.
        因为每次推导只依赖于其相邻的元素,所以可以转化为一位数组,公式如下
        dp[i] = max(total-dp[i-1],total-dp[i]),dp[i]表示0~i的最大值
        --------------
        在实现时,i和j的计算公式耗费了太多的思考时间
        :param nums:
        :return:
        """
        dp = [n for n in nums]
        for i in range(len(nums) - 2, -1, -1):
            index = i
            for j in range(len(nums) - 1, len(nums) - 2 - i, -1):
                total = sum(nums[index:j + 1])
                dp[j] = max(total - dp[j - 1], total - dp[j])
                index -= 1
        return dp[len(nums) - 1] >= sum(nums) - dp[len(nums) - 1]

    def PredictTheWinner_3(self, nums):
        """
        参考思路,dp思路:
        https://leetcode.com/articles/predict-the-winner/
        公式为:
        1.dp[i][j]为从i到j的最大值
        2.sum = sum(num[i]..num[j]),闭区间
        3.dp[i][j] = max(sum-dp[i+1][j],sum-dp[i][j-1])
        4.返回结果为 dp[0][len(nums)]>sum(nums)-dp[0][len(nums)]
        -----------
        验证通过,性能不错
        Runtime: 36 ms, faster than 85.70% of Python3 online submissions for Predict the Winner.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Predict the Winner.
        :param nums:
        :return:
        """
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]

        # 以平行于对角线的方式进行迭代
        for i in range(len(nums)):
            index_i = 0
            for j in range(i + 1, len(nums)):
                total = sum(nums[index_i:j + 1])
                dp[index_i][j] = max(total - dp[index_i + 1][j], total - dp[index_i][j - 1])
                index_i += 1
        return dp[0][len(nums) - 1] >= sum(nums) - dp[0][len(nums) - 1]

    def PredictTheWinner_2(self, nums):
        """
        在PredictTheWinner_1()基础上,进行优化.
        引入缓存,避免不必要的重复计算
        ----------------
        验证通过,性能一般.
        Runtime: 48 ms, faster than 19.14% of Python3 online submissions for Predict the Winner.
        Memory Usage: 13.3 MB, less than 60.00% of Python3 online submissions for Predict the Winner.
        时间复杂度:O(N*N)
        空间复杂度:O(N*N)
        :param nums:
        :return:
        """

        def get_max(arr, total):
            """得到arr条件下第一个选择的选手(可能是player1或player2)可以得到的最大值"""
            if not arr or len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            key = str(arr)
            if cache[key] > 0:
                return cache[key]
            cache[key] = max(total - get_max(arr[1:], total - arr[0]), total - get_max(arr[:-1], total - arr[-1]))
            return cache[key]

        cache = collections.defaultdict(int)
        sum_all = sum(nums)
        max_player1 = get_max(nums, sum_all)
        return max_player1 >= sum_all - max_player1

    def PredictTheWinner_1(self, nums):
        """
        dp问题,公式如下:
        设T=sum(nums);f(nums)为第一个选择的player拿到的最大score,注意:在迭代中第一个选择的player可是是player1也可能是player2
        存在以下步骤:
        1.player1只有两种选择,第0个或者第n-1个.
        a.如果player1选择第0个,当满足nums[0]+(T-nums[0])-f(nums[1:])>f(nums[1:])时,返回True;
        b.如果player1选择第n-1个,当满足nums[n-1]+(T-nums[n-1])-f(nums[:-1])>f(nums[:-1])时,返回True;
        c.其他情况返回False
        d.每一次迭代T都是变化的
        2.f()方法可以递归调用,当只剩下一个数字时,直接返回该数字;否则返回T-f(nums[1:])或T-f(nums[:-1])的最大值.
        ------------------
        验证失败,原因:Time Limit Exceeded
        验证结果:40 / 61 test cases passed.超时
        时间复杂度:O(2^N)
        :param nums:
        :return:
        """

        def get_max(arr, total):
            """得到arr条件下第一个选择的选手(可能是player1或player2)可以得到的最大值"""
            if not arr or len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            return max(total - get_max(arr[1:], total - arr[0]), total - get_max(arr[:-1], total - arr[-1]))

        sum_all = sum(nums)
        max_player1 = get_max(nums, sum_all)
        return max_player1 >= sum_all - max_player1


def main():
    # nums = [0]
    # ret = Solution().PredictTheWinner(nums)
    # print(ret)
    # print("--------------------")

    # nums = [2, 2, 2, 2]
    # ret = Solution().PredictTheWinner(nums)
    # print(ret)
    # print("--------------------")

    nums = [1, 5, 2]
    ret = Solution().PredictTheWinner(nums)
    print(ret)
    print("--------------------")

    nums = [1, 5, 233, 7]
    ret = Solution().PredictTheWinner(nums)
    print(ret)
    print("--------------------")

    nums = [9, 1, 5, 233, 7]
    ret = Solution().PredictTheWinner(nums)
    print(ret)
    print("--------------------")

    nums = [504, 427, 95, 397, 468, 485, 326, 112, 296, 290, 106, 148, 12, 334, 23, 296, 122, 187, 141, 187]
    ret = Solution().PredictTheWinner(nums)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
