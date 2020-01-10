"""
https://leetcode.com/problems/maximum-average-subarray-i/
643. Maximum Average Subarray I
Easy
---------------
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value.
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75

Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution:
    def findMaxAverage(self, nums, k):
        return self.findMaxAverage_1(nums, k)

    def findMaxAverage_1(self, nums, k):
        """
        滑动窗口
        1.初始计算[0:k-1]的sum为last_sum
        2.遍历[1:len(nums-k)],每次用last_sum-nums[i-1]+nums[i+k],使max_sum=max(max_sum,last_sum)
        3.返回max_sum/k
        ------------
        验证通过,性能一般
        Runtime: 1012 ms, faster than 11.01% of Python3 online submissions for Maximum Average Subarray I.
        Memory Usage: 16.1 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
        :param nums:
        :param k:
        :return:
        """
        if not nums and 0 >= k > len(nums):
            return None
        last_sum = max_sum = sum(nums[0:k])
        for i in range(1, len(nums) - k + 1):
            last_sum = last_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, last_sum)
        return max_sum / k


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    ret = Solution().findMaxAverage(nums, k)
    print(ret)
    print(ret == 12.75)
    print("--------------------")

    [1, 12, -5, -6, 50, 3, 35, 4, 5, 6, 7, 8, ]


if __name__ == "__main__":
    main()
