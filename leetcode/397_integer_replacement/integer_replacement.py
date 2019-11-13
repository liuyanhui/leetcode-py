"""
https://leetcode.com/problems/integer-replacement/
397. Integer Replacement
Medium
------------------
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:
8
Output:
3
Explanation:
8 -> 4 -> 2 -> 1

Example 2:
Input:
7
Output:
4
Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
import collections


class Solution:
    def integerReplacement(self, n):
        return self.integerReplacement_1(n)

    def integerReplacement_1(self, n):
        """
        dp问题,公式为:
        f(n)=f(n/2)+1,n为even
        f(n)=min(f(n+1),f(n-1))+1,n为odd
        ----------
        验证通过,性能一般,耗时较长:
        Runtime: 316 ms, faster than 18.48% of Python3 online submissions for Integer Replacement.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Integer Replacement.
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        cache_dict = collections.defaultdict(int)

        def do_dp(m):
            if cache_dict[m] > 0:
                return cache_dict[m]
            if m == 1:
                return 0
            if m % 2 == 0:
                return do_dp(m // 2) + 1
            else:
                return min(do_dp(m + 1), do_dp(m - 1)) + 1

        return do_dp(n)

    def integerReplacement_2(self, n):
        """
        其他方案:
        https://leetcode.com/problems/integer-replacement/discuss/87920/A-couple-of-Java-solutions-with-explanations
        https://leetcode.com/problems/integer-replacement/discuss/87928/Java-12-line-4(5)ms-iterative-solution-with-explanations.-No-other-data-structures.
        https://leetcode.com/problems/integer-replacement/discuss/87948/Python-O(log-n)-time-O(1)-space-with-explanation-and-proof
        :param n:
        :return:
        """
        pass


def main():
    ret = Solution().integerReplacement(0)
    print(ret)
    print("--------------------")

    ret = Solution().integerReplacement(1)
    print(ret)
    print("--------------------")

    ret = Solution().integerReplacement(8)
    print(ret)
    print("--------------------")

    ret = Solution().integerReplacement(7)
    print(ret)
    print("--------------------")

    ret = Solution().integerReplacement(10)
    print(ret)
    print("--------------------")

    ret = Solution().integerReplacement(57979)
    print(ret)
    print(ret == 21)
    print("--------------------")


if __name__ == "__main__":
    main()
