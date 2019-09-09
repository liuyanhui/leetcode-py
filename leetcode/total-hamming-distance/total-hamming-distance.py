class Solution:
    """
    https://leetcode.com/problems/total-hamming-distance/
    477. Total Hamming Distance
    Medium
    """

    def totalHammingDistance(self, nums):
        return self.totalHammingDistance_2(nums)

    def totalHammingDistance_1(self, nums):
        """
        暴力法,必然会导致超时
        :param nums:
        :return:
        """
        ret = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ret += self.hammingDistance(nums[i], nums[j])
        return ret

    def hammingDistance(self, x, y):
        ret = 0
        xor = x ^ y
        while xor > 0:
            ret += xor & 1
            xor >>= 1
        return ret

    def totalHammingDistance_2(self, nums):
        """
        参考思路:
        https://leetcode.com/problems/total-hamming-distance/discuss/96243/Share-my-O(n)-C%2B%2B-bitwise-solution-with-thinking-process-and-explanation
        解释如下:
        一般来说整数有32bit.数组中所有整数的二进制表示的第i位,非0即1.所以我们可以记录如下:
        0位      M0      N0
        1位      M1      N1
        ...
        31位     M31     N31
        其中Mi表示第i位是1的数字的个数,Ni表示第i位是0的数字的个数,且满足Ni+Mi=len(nums).
        Mi*Ni就是第i位的Hamming distance总和,那么sum(Ni*Mi)就是所求,即sum(Ni*(len(nums)-Ni))就是所求.
        注:
        各个位的total Hamming distance是独立的,所以可以以位为单位分别计算后再求和
        :param nums:
        :return:
        """
        if nums is None or len(nums) == 0:
            return 0
        ret = 0
        for i in range(32):
            x = 0
            for n in nums:
                x += (n >> i) & 1
            ret += x * (len(nums) - x)
        return ret


def main():
    nums = [4, 14, 2]
    ret = Solution().totalHammingDistance(nums)
    print(ret)
    print("----------")

    nums = [i + 1000000 for i in range(10 ** 4)]
    # print(len(nums))
    ret = Solution().totalHammingDistance(nums)
    print(ret)
    print("----------")


if __name__ == "__main__":
    main()
