"""
https://leetcode.com/problems/4sum-ii/
454. 4Sum II
Medium
--------------
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""

import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        return self.fourSumCount_1(A, B, C, D)

    def fourSumCount_1(self, A, B, C, D):
        """
        two sum的变化版本
        验证通过.
        Runtime: 304 ms, faster than 56.48% of Python3 online submissions for 4Sum II.
        Memory Usage: 55.5 MB, less than 8.33% of Python3 online submissions for 4Sum II.
        :param A:
        :param B:
        :param C:
        :param D:
        :return:
        """
        if not A or not B or not C or not D:
            return 0
        count = 0
        cache = collections.defaultdict(int)
        for a in A:
            for b in B:
                cache[a + b] += 1
        for c in C:
            for d in D:
                count += cache[-(c + d)]
                # 上面的这行用来替换下面的被注释的代码
                # if cache[-(c + d)] > 0:
                #     count += cache[-(c + d)]
        return count

    def fourSumCount_brute(self, A, B, C, D):
        """
        暴力法.Time Complexity:O(N**4)
        必然无法通过验证.
        这个方案没有利用ABCD的长度相等这个条件.
        :param A:
        :param B:
        :param C:
        :param D:
        :return:
        """
        if not A or not B or not C or not D:
            return 0
        count = 0
        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a + b + c + d == 0:
                            count += 1
        return count


def main():
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    ret = Solution().fourSumCount(A, B, C, D)
    print(ret)
    print(ret == 2)
    print('--------------------')

    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    ret = Solution().fourSumCount(A, B, C, D)
    print(ret)
    print(ret == 6)
    print('--------------------')

    # A = [-1, -1]
    # B = [-1, 1]
    # C = [-1, 1]
    # D = [1, -1]
    # ret = Solution().fourSumCount(A, B, C, D)
    # print(ret)
    # print(ret == 6)
    # print('--------------------')


if __name__ == "__main__":
    main()
