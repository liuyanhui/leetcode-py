"""
https://leetcode.com/problems/number-of-1-bits/
191. Number of 1 Bits
Easy
----------------
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.hammingWeight_2(n)

    def hammingWeight_1(self, n):
        """
        参考思路:https://leetcode.com/problems/number-of-1-bits/solution/
        :param n:
        :return:
        """
        return bin(n).count('1')

    def hammingWeight_2(self, n):
        """
        参考思路:https://leetcode.com/problems/number-of-1-bits/solution/
        Bit Manipulation:
        n &= (n - 1)
        :param n:
        :return:
        """
        c = 0
        while n:
            n &= (n - 1)
            c += 1
        return c


def main():
    # ret = Solution().hammingWeight(0)
    # print(ret)
    # print("--------------------")
    #
    m = 0b11111111111111111111111111111101
    ret = Solution().hammingWeight(m)
    print(ret)
    print("--------------------")
    #
    # ret = Solution().hammingWeight(-1)
    # print(ret)
    # print("--------------------")
    #
    # ret = Solution().hammingWeight(-3)
    # print(ret)
    # print("--------------------")

    pass


if __name__ == "__main__":
    main()
