"""
https://leetcode.com/problems/longest-increasing-subsequence/
300. Longest Increasing Subsequence
Medium
-----------
Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        return self.lengthOfLIS_recursive(nums)

    def lengthOfLIS_dp2(self, nums):
        """
        lengthOfLIS_dp()的优化版本.
        参考思路:
        https://leetcode.com/problems/longest-increasing-subsequence/solution/
        https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/

        Time Complexity:O(N*logN)
        Space Complexity:O(N)
        ---------------
        验证通过
        Runtime: 32 ms, faster than 98.84% of Python3 online submissions for Longest Increasing Subsequence.
        Memory Usage: 14.1 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
        :param nums:
        :return:
        """
        if not nums and len(nums) <= 0:
            return 0
        dp = []
        for n in nums:
            # binarysearch
            l, r = 0, len(dp) - 1
            while l <= r:
                mid = (l + r) // 2
                if dp[mid] < n:
                    l = mid + 1
                elif dp[mid] > n:
                    r = mid - 1
                else:
                    l = mid
                    break
            if len(dp) == l:
                dp.append(n)
            else:
                dp[l] = n
        return len(dp)

    def lengthOfLIS_dp(self, nums):
        """
        dp思路,参考官方的解题思路.
        关键点在于:dp[i]是以i为结尾的最大LIS的值.我之前的方法lengthOfLIS_1()的dp定义有误,导致无法得到正确的解.
        --------------
        Time complexity O(N*2)
        Space Complexity O(N)
        Runtime: 1132 ms, faster than 47.80% of Python3 online submissions for Longest Increasing Subsequence.
        Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
        -----
        如何才能优化到N*logN的时间复杂度???
        :param nums:
        :return:
        """
        if not nums and len(nums) <= 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            t_d = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    t_d = max(t_d, dp[j] + 1)
            dp[i] = t_d
        return max(dp)

    def lengthOfLIS_recursive(self, nums):
        """
        递归+暴力法.使用递归栈+循环的思路.
        -------
        时间复杂度:O(N^N)
        验证失败,Time Limit Exceeded
        根据BUD方法,这种暴力法思路中有大量的重复计算,如果去掉这些重复计算,可以优化性能,降低耗时.
        :param nums:
        :return:
        """
        if not nums and len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return 1
        ret = [0]
        stack_list = [-999999]

        def fun_recursive(nums_l, index, cur_stack):
            for i in range(index, len(nums_l)):
                if nums_l[i] > cur_stack[-1]:
                    cur_stack.append(nums[i])
                    ret[0] = max(ret[0], len(cur_stack) - 1)
                    fun_recursive(nums_l, i + 1, cur_stack)
                    cur_stack.pop()
                else:
                    pass

        fun_recursive(nums, 0, stack_list)
        return ret[0]

    def lengthOfLIS_1(self, nums):
        """
        这个问题从0开始计算的解空间太大,从后向前计算的复杂度更低,也更好理解.
        是一个dp问题,公式如下:
        从后向前遍历
        if nums[i]<min  => dp[i]=dp[i+1]+1, min=nums[i]
        if nums[i]>=min => dp[i]=dp[i+1]
        dp[0]就是结果
        ------------
        验证失败,在输入为[1, 3, 6, 7, 9, 4, 10, 5, 6]的情况下验证失败.这种解法只是解决了从[i,tail]的最优解,无法覆盖[i,j]的全部情况.
        :param nums:
        :return:
        """
        if not nums and len(nums) <= 0:
            return 0
        dp = [0] * (len(nums) + 1)
        min_t = 9999999
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= min_t:
                dp[i] = dp[i + 1]
            elif nums[i] < min_t:
                min_t = nums[i]
                dp[i] = 1 + dp[i + 1]
        print(dp)
        return dp[0]


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    ret = Solution().lengthOfLIS(nums)
    print(ret)
    print(ret == 4)
    print("--------------------")

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    ret = Solution().lengthOfLIS(nums)
    print(ret)
    print(ret == 6)
    print("--------------------")

    nums = [0]
    ret = Solution().lengthOfLIS(nums)
    print(ret)
    print(ret == 1)
    print("--------------------")

    nums = [-2, -1]
    ret = Solution().lengthOfLIS(nums)
    print(ret)
    print(ret == 2)
    print("--------------------")

    nums = [1, 2]
    ret = Solution().lengthOfLIS(nums)
    print(ret)
    print(ret == 2)
    print("--------------------")


if __name__ == '__main__':
    main()
