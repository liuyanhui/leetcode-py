"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
718. Maximum Length of Repeated Subarray
Medium
---------------
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3

Explanation:
The repeated subarray with maximum length is [3, 2, 1].

Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
import collections

class Solution:
    def findLength(self, A, B):
        return self.findLength_brtue_cache(A, B)

    def findLength_dp(self, A, B):
        """
        参考思路:https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode/
        采用DP思路
        定义dp[i][j]为从A[:i]和B[:j]的最长公共子串长度.那么当A[i+1]=B[j+1]时,dp[i+1][j+1]=dp[i][j]+1,否则dp[i+1][j+1]=0
        -----------
        验证通过:
        Runtime: 5200 ms, faster than 32.29% of Python3 online submissions for Maximum Length of Repeated Subarray.
        Memory Usage: 39.8 MB, less than 16.67% of Python3 online submissions for Maximum Length of Repeated Subarray.
        :param A:
        :param B:
        :return:
        """
        if not A or not B:
            return 0

        dp=[[0 for i in range(len(B)+1)] for i in range(len(A)+1)]
        ret = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    ret = max(ret,dp[i+1][j+1])

        return ret

    def findLength_brtue_cache(self, A, B):
        """
        findLength_brute()的优化版本,缓存重复计算的部分
        --------------
        验证失败,超时.
        :param A:
        :param B:
        :return:
        """
        if not A or not B:
            return 0
        max_sub_len = 0
        cache = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                ti, tj = i, j
                key = str(ti)+":"+str(tj)
                if cache[key] > 0:
                    ti += cache[key]
                else:
                    while ti < len(A) and tj < len(B) and A[ti] == B[tj]:
                        ti += 1
                        tj += 1
                    cache[key] = ti - i
                max_sub_len = max(max_sub_len, ti - i)
        return max_sub_len

    def findLength_brute(self, A, B):
        """
        暴力思路.
        时间复杂度:O(N*M*N)
        根据BUD思路,存在重复计算的部分.即,从A[i]和B[j]开始比较存在重复计算的情况.
        :param A:
        :param B:
        :return:
        """
        if not A or not B:
            return 0
        max_sub_len = 0
        for i in range(len(A)):
            for j in range(len(B)):
                ti, tj = i, j
                while ti < len(A) and tj < len(B) and A[ti] == B[tj]:
                    ti += 1
                    tj += 1
                max_sub_len = max(max_sub_len, ti - i)
        return max_sub_len


def main():
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    ret = Solution().findLength(A, B)
    print(ret)
    print(ret == 3)
    print("--------------------")

    A = [1, 2, 3, 2, 1]
    B = [1, 4, 7]
    ret = Solution().findLength(A, B)
    print(ret)
    print(ret == 1)
    print("--------------------")

    A = [1, 2, 3, 2, 1]
    B = [1, 1, 2]
    ret = Solution().findLength(A, B)
    print(ret)
    print(ret == 2)
    print("--------------------")

    A = [1, 1, 2, 3, 2, 1]
    B = [2, 1, 1, 2]
    ret = Solution().findLength(A, B)
    print(ret)
    print(ret == 3)
    print("--------------------")

    A = [8, 1, 1, 2, 3, 2, 1]
    B = [2, 1, 1, 2]
    ret = Solution().findLength(A, B)
    print(ret)
    print(ret == 3)


if __name__ == "__main__":
    main()
