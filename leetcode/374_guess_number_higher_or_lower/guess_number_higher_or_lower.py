"""
https://leetcode.com/problems/guess-number-higher-or-lower/
374. Guess Number Higher or Lower
Easy
-------------------------
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6
"""


class Solution:
    def guessNumber(self, n):
        return self.guessNumber_1(n)

    def guessNumber_1(self, n):
        """
        采用二分查找的方式
        -----------
        验证通过
        :param n:
        :return:
        """
        if n < 1:
            return 0
        l, r = 1, n
        while l < r:
            c = (l + r) // 2
            g = self.guess(c)
            if g == 0:
                return c
            elif g == 1:
                l = c + 1
            else:
                r = c - 1
        return l

    def guess(self, num):
        pick = 21
        if pick > num:
            return 1
        elif pick < num:
            return -1
        else:
            return 0


def main():
    n = 100
    ret = Solution().guessNumber(n)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
