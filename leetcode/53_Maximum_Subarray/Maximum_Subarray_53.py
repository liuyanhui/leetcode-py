"""
53. Maximum Subarray
Medium
------------------------------
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        return self.maxSubArray_1(nums)

    def maxSubArray_1(self, nums: list) -> int:
        """
        Round 3
        Score[2] Lower is harder

        Thinking：
        1.slide window solution

        验证通过:
        Runtime 551 ms Beats 89.47%
        Memory 31.88 MB Beats 18.56%

        Args:
            nums:

        Returns:

        """
        ret = -99999
        sum_t = 0
        for n in nums:
            if n >= 0:  # sum增加,sum_t可能大于0也可能小于0
                sum_t = max(n, sum_t + n)
            elif sum_t + n <= 0:  # sum不增加，sum小于0
                sum_t = n
            else:  # sum不增加，sum大于0
                sum_t += n
            ret = max(ret, sum_t, n)
        return ret


def do_func(nums: list, expect: int):
    ret = Solution().maxSubArray(nums)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    do_func([1], 1)
    do_func([5, 4, -1, 7, 8], 23)
    do_func([-1], -1)
    do_func([-1, -2, -2], -1)
    do_func([-4, -1, -2, -2], -1)


if __name__ == '__main__':
    main();
