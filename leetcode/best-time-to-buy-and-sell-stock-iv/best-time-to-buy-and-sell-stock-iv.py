class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
    188. Best Time to Buy and Sell Stock IV
    hard
    """

    def maxProfit(self, k: int, prices):
        return self.maxProfit_3(k, prices)

    def maxProfit_1(self, k, prices):
        """
        验证失败，原因:Time Limit Exceeded
        """
        if k <= 0 or prices is None or len(prices) <= 1:
            return 0
        max_k = min(len(prices) - 1, k)
        g = [[0 for i in range(max_k + 1)] for i in range(len(prices))]
        l = [[0 for i in range(max_k + 1)] for i in range(len(prices))]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, max_k + 1):
                l[i][j] = max(g[i - 1][j - 1] + max(0, diff), l[i - 1][j] + diff)
                # print(l[i][j])
                g[i][j] = max(g[i - 1][j], l[i][j])
                # print(g[i][j])
                # print("==========")
        return g[len(prices) - 1][max_k]

    def maxProfit_2(self, k, prices):
        """
        maxProfit_1的简化版本，减少使用的变量
        验证失败，原因:Time Limit Exceeded
        """
        if k <= 0 or prices is None or len(prices) <= 1:
            return 0
        max_k = min(len(prices) - 1, k)
        g = [0] * (max_k + 1)
        l = [0] * (max_k + 1)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, max_k + 1):
                g[j] = max(g[j], l[j])
                # print(g[j])
                l[j] = max(g[j - 1] + max(0, diff), l[j] + diff)
                # print(l[j])
                # print("==========")
            g[j] = max(g[j], l[j])
        # print(str(g))
        return g[max_k]

    def maxProfit_3(self, k, prices):
        """
        参考了discuss中的方案，绕过TLE的用例，非常巧妙，解决了特定情况下的时间复杂度，但是没有解决本质问题。
        参考文档：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
        """
        if k <= 0 or prices is None or len(prices) <= 1:
            return 0

        if k >= len(prices) // 2:
            return self.quick_find(k, prices)

        max_k = min(len(prices) - 1, k)
        g = [0] * (max_k + 1)
        l = [0] * (max_k + 1)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, max_k + 1):
                g[j] = max(g[j], l[j])
                # print(g[j])
                l[j] = max(g[j - 1] + max(0, diff), l[j] + diff)
                # print(l[j])
                # print("==========")
            g[j] = max(g[j], l[j])
        # print(str(g))
        return g[max_k]

    def quick_find(self, k, prices):
        """
        参考了discuss中的方案，绕过TLE的用例，非常巧妙，解决了特定情况下的时间复杂度，但是没有解决本质问题。
        参考文档：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
        """
        ret = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            ret = ret + max(0, tmp)
        return ret
