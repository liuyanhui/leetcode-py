class Solution:
    """
    https://leetcode.com/problems/single-number-iii/
    260. Single Number III
    medium
    """
    """
    一个简单的方案:
    可以使用hashtable缓存数字出现的次数.第一次出现加入hashtable,第二次出现从hashtable中删除.
    最后剩下的数字就是答案.但是该方案不满足,constant space complexity的要求.
    """

    def singleNumber(self, nums):
        return self.singleNumber_1(nums)

    def singleNumber_1(self, nums):
        """
        参考思路:
        https://leetcode-cn.com/problems/single-number-iii/solution/cai-yong-fen-zhi-de-si-xiang-jiang-wen-ti-jiang-we/
        https://leetcode.com/problems/single-number-iii/discuss/326622/All-In-One-Summary-(Single-Number-I-II-III)
        :param nums:
        :return:
        """
        xor = 0
        for n in nums:
            xor ^= n
        # 利用xor的特点.
        # 数字xor中某位上为1时,该位在a和b中必然是不同的.所以用xor中某位为1,其他位都为0的数字作为mask.
        # 该mask把输入的数组分为两类,此时该问题退化为single-number问题
        mask = self.getSpecialOne(xor)
        # mask = xor & -xor
        a, b = 0, 0
        for n in nums:
            if n & mask > 0:
                a ^= n
            else:
                b ^= n
        return [a, b]

    def getSpecialOne(self, n):
        """
        获取n的最后一位为1,其他位为0的数字
        :param n:
        :return:
        """
        for i in range(32):
            if (n & (1 << i)) > 0:
                return 1 << i


def main():
    a = [1, 2, 1, 3, 2, 5]
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")

    a = [-1, 2, -1, -3, 2, 5]
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")

    # b = 2
    # ret = Solution().getSpecialOne(b)
    # print(ret)


if __name__ == "__main__":
    main()
