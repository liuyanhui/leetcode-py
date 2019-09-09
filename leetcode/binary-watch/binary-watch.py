class Solution:
    """
    https://leetcode.com/problems/binary-watch/
    401. Binary Watch
    Easy
    """

    def readBinaryWatch(self, num):
        return self.readBinaryWatch_5(num)

    def readBinaryWatch_1(self, num):
        """
        本题虽然是easy难度,但是如果思路不对是很难做出来的.
        穷举法是最简单的方法之一.参考思路如下:
        https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python%2BJava
        :param num:
        :return:
        """
        if 0 > num >= 10:
            return []
        ret = []
        for h in range(12):
            for m in range(60):
                if self.getBinaryOneCount(h) + self.getBinaryOneCount(m) == num:
                    ret.append("%d:%02d" % (h, m))

        return ret

    def getBinaryOneCount(self, num):
        """
        获取num中二进制各位=1的数量
        :param num:
        :return:
        """
        tmp = num
        count = 0
        while tmp > 0:
            count += tmp & 1
            tmp >>= 1
        return count

    def readBinaryWatch_2(self, num):
        """
        方法readBinaryWatch_1的简化版,
        :param num:
        :return:
        """
        if 0 > num >= 10:
            return []
        ret = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    ret.append("%d:%02d" % (h, m))

        return ret

    def readBinaryWatch_3(self, num):
        """
        方法readBinaryWatch_1的最简版
        参考如下:
        https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python%2BJava
        :param num:
        :return:
        """
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]

    def readBinaryWatch_4(self, num):
        """
        与前面的方面思路完全不同,不是采用穷举法,而是采用类似推导/演绎的方法.
        为了避免多重嵌套循环,采用了递归(栈)进行遍历计算.
        采用permutation and combination的思路.
        参考文档:
        https://leetcode.com/problems/binary-watch/discuss/88456/3ms-Java-Solution-Using-Backtracking-and-Idea-of-%22Permutation-and-Combination%22
        :param num:
        :return:
        """
        ret = []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        for i in range(num + 1):
            # 分治法
            h_combination = self.generateTime(hours, i)
            m_combination = self.generateTime(minutes, num - i)

            for h in h_combination:
                for m in m_combination:
                    if sum(h) < 12 and sum(m) < 60:
                        ret.append("%d:%02d" % (sum(h), sum(m)))

        return ret

    def generateTime(self, nums, count):
        """
        采用Combination思路
        :param nums:
        :param count:
        :return:
        """
        ret = []
        self.generateTimeCombination(nums, count, 0, [], ret)
        return ret

    def generateTimeCombination(self, nums, count, beg, present, ret):
        if count == 0:
            ret.append(present.copy())
            return
        for i in range(beg, len(nums)):
            present.append(nums[i])
            self.generateTimeCombination(nums, count - 1, i + 1, present, ret)
            present.remove(nums[i])

    def readBinaryWatch_5(self, num):
        """
        readBinaryWatch_4的代码简化版本.
        主要是优化sum(h) < 12 ,sum(m), present三个部分
        参考文档:
        https://leetcode.com/problems/binary-watch/discuss/88456/3ms-Java-Solution-Using-Backtracking-and-Idea-of-%22Permutation-and-Combination%22
        :param num:
        :return:
        """
        ret = []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        for i in range(num + 1):
            # 分治法
            h_combination = self.generateTime_5(hours, i)
            m_combination = self.generateTime_5(minutes, num - i)

            for h in h_combination:
                for m in m_combination:
                    if h < 12 and m < 60:
                        ret.append("%d:%02d" % (h, m))

        return ret

    def generateTime_5(self, nums, count):
        """
        采用Combination思路
        :param nums:
        :param count:
        :return:
        """
        ret = []
        self.generateTimeCombination_5(nums, count, 0, 0, ret)
        return ret

    def generateTimeCombination_5(self, nums, count, beg, present, ret):
        if count == 0:
            ret.append(present)
            return
        for i in range(beg, len(nums)):
            self.generateTimeCombination_5(nums, count - 1, i + 1, present + nums[i], ret)


def main():
    a = 1
    ret = Solution().readBinaryWatch(a)
    print(ret)
    print("------------")

    a = 2
    ret = Solution().readBinaryWatch(a)
    print(ret)
    print("------------")

    # nums = [1, 2, 4, 8]
    # ret = []
    # Solution().permutation_combination(nums, 3, 0, ret)
    # print(ret)


if __name__ == "__main__":
    main()
