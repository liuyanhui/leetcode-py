"""
https://leetcode.com/problems/counting-bits/
338. Counting Bits
Medium
----------------
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


class Solution:
    def countBits(self, num):
        return self.countBits_dp_2(num)

    def countBits_brute(self, num):
        """
        暴力法
        从[0,num]进行循环计算每个数字的二进制中的1的个数.
        这个方法应该可以优化的,因为相邻数字的1的个数应该是有规律的
        -------
        性能较差,采用BUD进行优化
        :param num:
        :return:
        """
        if num < 0:
            return []

        def calc_1_count(n):
            return bin(n).count("1")

        ret = []
        for i in range(num + 1):
            ret.append(calc_1_count(i))
        return ret

    def countBits_dp(self, num):
        """
        通过举例.列出1~16的二进制表示,可以看出规律.
        1.假设2^i~2^(i+1)作为一个区间,后一个区间(如:2^i~2^(i+1))的数字个数与前面所有区间(2^0~2^i)的个数相等.
        如:当前区间的数字为[9-16],前面所有区间的数字为[1-8],都是8个数字.
        2.可总结出公式为 r[j]=r[j-2^i]+1,其中 2^i<j<=2^(i+1),r[i]表示数字i中的bit1的个数.即r[12]=r[12-8]+1=r[4]+1=2
        -------------
        验证通过:
        Runtime: 116 ms, faster than 30.68% of Python3 online submissions for Counting Bits.
        Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.
        :param num:
        :return:
        """
        if num < 0:
            return []
        ret = [0 for i in range(num + 1)]
        k = 0
        for i in range(1, num + 1):
            if i == 2 ** k:  # 这里可以优化,避免每次重复计算
                ret[i] = 1
                k += 1
                continue
            ret[i] = ret[i - 2 ** (k - 1)] + 1  # 这里可以优化,避免每次都重复计算
        return ret

    def countBits_dp_2(self, num):
        """
        countBits_dp()的优化版本
        -------------
        验证通过,性能有提升:
        Runtime: 96 ms, faster than 74.41% of Python3 online submissions for Counting Bits.
        Memory Usage: 19.6 MB, less than 5.00% of Python3 online submissions for Counting Bits.
        :param num:
        :return:
        """
        if num < 0:
            return []
        ret = [0 for i in range(num + 1)]
        bound = 1
        for i in range(1, num + 1):
            # 思路1:
            if i == bound:
                ret[i] = 1
                bound *= 2
                continue
            ret[i] = ret[i - bound // 2] + 1
            # 其他思路1:https://leetcode.com/problems/counting-bits/discuss/79539/Three-Line-Java-Solution
            # ret[i] = ret[i >> 1] + (i & 1)
            # 其他思路2:https://leetcode.com/problems/counting-bits/discuss/79527/Four-lines-C%2B%2B-time-O(n)-space-O(n)
            # ret[i] = ret[i&(i-1)] + 1;
        return ret


def main():
    ret = Solution().countBits(0)
    print(ret)
    print("--------------------")

    ret = Solution().countBits(2)
    print(ret)
    print("--------------------")

    ret = Solution().countBits(5)
    print(ret)
    print("--------------------")

    ret = Solution().countBits(50000)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
