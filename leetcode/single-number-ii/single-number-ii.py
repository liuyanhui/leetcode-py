class Solution:
    """
    https://leetcode.com/problems/single-number-ii/
    137. Single Number II
    medium

    解决方案综述:
    https://leetcode.com/problems/single-number-iii/discuss/326622/All-In-One-Summary-(Single-Number-I-II-III)
    """

    def singleNumber(self, nums):
        return self.singleNumber_3(nums, 3)

    def singleNumber_1(self, nums, k):
        """
        用hashtable保存数字的出现次数,出现k次后删除该数字.
        这种方法使用了extra memory,所以不符合规定
        :param nums:
        :return:
        """
        h = {}
        for n in nums:
            if n not in h:
                h[n] = 1
            else:
                h[n] += 1
                if h[n] == k:
                    h.pop(n)
        return list(h.keys())[0]

    def singleNumber_2(self, nums, k):
        """
        参考Discuss区的一种方法思路,时间复杂度O(32*n),空间复杂度O(1).思路如下:
        大神使用了一种统计的方法，不过不是我等平常思维的统计每个数出现了几次，
        而是开了一个长度为32的数组，统计每个二进制位出现了几次，
        最后对3取模（如果是出现了K次就对K取模），取模完哪一位不是3的整倍数，
        就说明只出现了一次的那个数，在这个位上为1，最终可以求出最后的结果。
        参考文档:
        https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
        https://cloud.tencent.com/developer/article/1131946
        https://blog.csdn.net/jiadebin890724/article/details/23306837
        :param nums:
        :param k:
        :return:
        """
        ret1, ret2 = 0, 0
        for i in range(32):
            t = 0  # 正数
            m = 0  # 负数
            for n in nums:
                # 需要考虑负数,正数和负数的逻辑不同.负数是用补码存储的.
                if n >= 0:
                    t += (n >> i) & 1
                else:
                    m += (abs(n) >> i) & 1
            t %= k
            m %= k
            ret1 += t << i
            ret2 += m << i
            # print("i=%d,t=%d,ret=%d" % (i, t, ret1))

        return ret1 | -ret2

    def singleNumber_3(self, nums, k):
        """
        思路:https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
        异或运算的另一个含义是“二进制下不考虑进位的加法”：0+0 = 0， 1+1=0……
        我们联想到，是否可以通过某种运算$，使a $ a $ a = 0，0 $ a = a，即创建“三进制下不考虑进位的加法”，这样将整个arr遍历加和，留下来的就是那个只出现一次的数字（其余各位都出现了3x次，一定为0）。
        看到下面一堆与、或、非、异或运算应该很懵吧……下面一条条分析：
        ones记录至目前元素，各位元素出现1次的位置；
        twos记录至目前元素，各位元素出现2次的位置；
        threes记录至目前元素，各位元素出现3次的位置 每轮完成时，当threes里某位为1时（代表此位出现了3次），需要将ones twos的对应位清零。
        :param nums:
        :param k:
        :return:last-stone-weight
        """
        one, two, three = 0, 0, 0
        for n in nums:
            two |= one & n  # ones & n 提取两个数都为1的位，与twos作或操作保留出现2次的位
            one ^= n  # 当 ones 和 n 同时为 1 or 0 时，ones = 0，因为同时为1已经加到twos里了，这里不做count
            three = one & two  # 当ones和twos对应位都为1时，说明此位出现了3次
            one &= ~three  # three为1的位，将one和two对应位归零
            two &= ~three
        return one


def main():
    a = [2, 2, 3, 2]
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")

    a = [0, 1, 0, 1, 0, 1, 99]
    # print("a=", a)
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")

    a = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    ret = Solution().singleNumber(a)
    print(ret)
    print("-----------------")


if __name__ == "__main__":
    main()
