"""
66. Plus One
Easy
------------------------
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


class Solution:
    def plusOne(self, digits: list) -> list:
        return self.plusOne_1(digits)

    def plusOne_1(self, digits: list) -> list:
        """
        Round 3
        Score[5] Lower is harder

        验证通过

        Args:
            digits:

        Returns:

        """
        ret = []
        carry = 1
        for n in digits[::-1]:
            ret.append((n + carry) % 10)
            carry = (n + carry) // 10
        if carry > 0:
            ret.append(carry)
        return ret[::-1]


def do_func(digits: list, expect: list):
    ret = Solution().plusOne(digits)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([1, 2, 3], [1, 2, 4])
    do_func([4, 3, 2, 1], [4, 3, 2, 2])
    do_func([9], [1, 0])
    do_func([0], [1])


if __name__ == "__main__":
    main()
