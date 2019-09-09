class Solution:
    """
    123. Best Time to Buy and Sell Stock III
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
    hard

    参考资料，公有三种思路：
    https://blog.csdn.net/u012501459/article/details/46514309
    https://www.cnblogs.com/grandyang/p/4281975.html
    https://blog.csdn.net/linhuanmars/article/details/23236995
    """

    def maxProfit(self, prices):
        return self.maxProfit_6(prices)

    def maxProfit_1(self, prices):
        """
        参考思路:https://blog.csdn.net/linhuanmars/article/details/23236995
        局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值中取较大值.
        全局最优比较局部最优和前一天的全局最优.
        我们维护两种变量:
        1.一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），
        2.另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）。
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0
        k = 2
        l = [[0 for i in range(k + 1)] for i in range(len(prices))]
        g = [[0 for i in range(k + 1)] for i in range(len(prices))]
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            # 重点1: 注意这里不考虑j=0的情况,否则结果会有问题.也不需要考虑不交易的情况.
            for j in range(1, k + 1):
                # 重点2:推导公式
                l[i][j] = max(l[i - 1][j] + tmp, g[i - 1][j - 1] + max(0, tmp))
                g[i][j] = max(g[i - 1][j], l[i][j])
                # print("l[%d][%d]=%d" % (i, j, l[i][j]))
                # print("g[%d][%d]=%d" % (i, j, g[i][j]))
                # print("====================")
                ret = g[i][j]
        # print(str(l))
        # print(str(g))
        return ret

    def maxProfit_2(self, prices):
        """
        maxProfit_1的代码优化版本,主要是对l和g数组优化.由于l[i][j]和g[i][j]的计算只跟l[i-1]或g[i-1]有关,可以优化二维数组为以为数组
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0
        k = 2
        l = [0 for i in range(k + 1)]
        g = [0 for i in range(k + 1)]
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            # 重点1: 注意这里不考虑j=0的情况,否则结果会有问题.也不需要考虑不交易的情况.
            # 这里的循环和maxProfit_1不一样哦,由于覆盖的顺序关系,是j递减循环,
            # 我们需要j从2到1，这样可以取到正确的g[j-1]值，而非已经被覆盖过的值
            j = k
            while j >= 1:
                # 重点2:推导公式
                l[j] = max(l[j] + tmp, g[j - 1] + max(0, tmp))
                g[j] = max(g[j], l[j])
                j -= 1
                print("l[%d]=%d" % (j, l[j]))
                print("g[%d]=%d" % (j, g[j]))
                print("====================")
            ret = g[k]
        return ret

    def maxProfit_3(self, prices):
        """
        https://blog.csdn.net/u012501459/article/details/46514309中的解法一思路.
        1.两次股票交易的核心是可以定义一个交易点，在这个交易点之前可以做一次交易(赚的最大数目的钱为firstProf)，
        在这个交易点之后可以做一个交易(赚的最大数目的钱是secondProf)。那么要求的是max(firstProf+secondProf)。
        但是这个方法的时间复杂度是O(N^2)，空间复杂度是O(1)。
        leetcode中显示超时Time Limit Exceeded。
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0

        for i in range(len(prices)):
            # i天前最赚钱的交易
            fmax, fmin = 0, prices[0]
            for j in range(i):
                fmax = max(fmax, prices[j] - fmin)
                fmin = min(prices[j], fmin)

            # i天后最赚钱的交易
            smax, smin = 0, prices[i]
            for k in range(i, len(prices)):
                smax = max(smax, prices[k] - smin)
                smin = min(prices[k], smin)
            ret = max(ret, fmax + smax)

        return ret

    def maxProfit_4(self, prices):
        """
        https://blog.csdn.net/u012501459/article/details/46514309中的解法一思路.
        在maxProfit_3方法基础上进行优化
        1.两次股票交易的核心是可以定义一个交易点，在这个交易点之前可以做一次交易(赚的最大数目的钱为firstProf)，
        在这个交易点之后可以做一个交易(赚的最大数目的钱是secondProf)。那么要求的是max(firstProf+secondProf)。
        但是这个方法的时间复杂度是O(N^2)，空间复杂度是O(1)。leetcode中显示超时。
        2.可以使用两次扫描的方法避免上面的双重循环。
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0

        # 依次求出从0~i天的最大收益
        fasc_max = [0] * len(prices)
        fasc_min = prices[0]
        for i in range(1, len(prices)):
            fasc_min = min(fasc_min, prices[i])
            fasc_max[i] = max(fasc_max[i - 1], prices[i] - fasc_min)
        print(str(fasc_max))

        # 依次求出从j~n天的最大收益
        fdesc_max = [0] * len(prices)
        fdesc_tmp_max = prices[len(prices) - 1]
        for j in range(len(prices) - 1, 0, -1):
            t_index = j - 1
            fdesc_tmp_max = max(fdesc_tmp_max, prices[t_index])
            fdesc_max[t_index] = max(fdesc_max[j], fdesc_tmp_max - prices[t_index])
        print(str(fdesc_max))

        for i in range(1, len(prices)):
            # i天前最赚钱的交易
            fmax = fasc_max[i]
            # i天后最赚钱的交易
            smax = fdesc_max[i]
            ret = max(ret, fmax + smax)

        return ret

    def maxProfit_5(self, prices):
        """
        https://blog.csdn.net/u012501459/article/details/46514309中的解法二思路.
        第二种解法的核心是假设手上最开始只有0元钱，那么如果买入股票的价格为price，手上的钱需要减去这个price，如果卖出股票的价格为price，手上的钱需要加上这个price。
        花掉的钱是-price,卖掉的钱是+price

        它定义了4个状态：
        Buy1[i]表示前i天做第一笔交易买入股票后剩下的最多的钱；
        Sell1[i]表示前i天做第一笔交易卖出股票后剩下的最多的钱；
        Buy2[i]表示前i天做第二笔交易买入股票后剩下的最多的钱；
        Sell2[i]表示前i天做第二笔交易卖出股票后剩下的最多的钱；

        那么得出公式
        Sell2[i]=max{Sell2[i-1],Buy2[i-1]+prices[i]}
        Buy2[i]=max{Buy2[i-1],Sell[i-1]-prices[i]}
        Sell1[i]=max{Sell[i-1],Buy1[i-1]+prices[i]}
        Buy1[i]=max{Buy[i-1],-prices[i]}
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0
        length = len(prices)
        s2, b2, s1, b1 = [0] * length, [0] * length, [0] * length, [0] * length
        b1[0] = -prices[0]
        s1[0] = 0
        b2[0] = -prices[0]
        s2[0] = 0
        for i in range(1, len(prices)):
            # i = idx + 1
            b1[i] = max(b1[i - 1], -prices[i])
            s1[i] = max(s1[i - 1], b1[i - 1] + prices[i])
            b2[i] = max(b2[i - 1], s1[i - 1] - prices[i])
            s2[i] = max(s2[i - 1], b2[i - 1] + prices[i])
            # s2[i] = max(s2[i - 1], b2[i - 1] + prices[i])
            # b2[i] = max(b2[i - 1], s1[i - 1] - prices[i])
            # s1[i] = max(s1[i - 1], b1[i - 1] + prices[i])
            # b1[i] = max(b1[i - 1], -prices[i])
            ret = s2[i]
        print("b1=", str(b1))
        print("s1=", str(s1))
        print("b2=", str(b2))
        print("s2=", str(s2))
        return ret

    def maxProfit_6(self, prices):
        """
        maxProfit_5的代码简化版.
        根据公式可以看出,当前值只跟前一个值有关,所以可以不用数组存储中间数据
        :param prices:
        :return:
        """
        if prices is None or len(prices) <= 1:
            return 0
        ret = 0
        s2, b2, s1, b1 = 0, 0, 0, 0
        b1 = -prices[0]
        s1 = 0
        b2 = -prices[0]
        s2 = 0
        for i in range(1, len(prices)):
            s2 = max(s2, b2 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s1 = max(s1, b1 + prices[i])
            b1 = max(b1, -prices[i])
        ret = s2
        print("b1=", str(b1))
        print("s1=", str(s1))
        print("b2=", str(b2))
        print("s2=", str(s2))
        return ret

    def maxProfit_error(self, prices):
        """
        在https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/基础上，进行了top2的筛选。即计算每个升值段，然后把各个小段排序，取top即可
        该方法有问题：用例[1,2,4,2,5,7,2,4,9,0]未通过
        """
        if prices is None or len(prices) == 0:
            return 0
        ret_list = []
        imin = last = prices[0]
        for p in prices[1:]:
            # print("p=%d,last=%d,imin=%d"%(p,last,imin))
            if p < last:
                ret_list.append(last - imin)
                imin = p
            last = p
        ret_list.append(last - imin)
        # print(str(ret_list))
        ret_list.sort(reverse=True)
        # print(str(ret_list))
        return sum(ret_list[0:2])


def main():
    # a = []
    # ret = Solution().maxProfit(a)
    # print(ret)

    print("----------")
    a = [1, 2, 3, 4, 5]
    print("a=", str(a))
    ret = Solution().maxProfit(a)
    print(ret)

    print("----------")
    a = [7, 6, 4, 3, 1]
    print("a=", str(a))
    ret = Solution().maxProfit(a)
    print(ret)

    # print("----------")
    # a = [3, 3, 5, 0, 0, 3, 1, 4]
    # print("a=",str(a))
    # ret = Solution().maxProfit(a)
    # print(ret)

    # print("----------")
    # a = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    # print("a=",str(a))
    # ret = Solution().maxProfit(a)
    # print(ret)


if __name__ == "__main__":
    main()
