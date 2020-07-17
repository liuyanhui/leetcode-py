"""
https://leetcode.com/problems/3sum-closest/
16. 3Sum Closest
Medium
----------------
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

import sys


class Solution:
    def threeSumClosest(self, nums, target):
        return self.threeSumClosest_1(nums, target)

    def threeSumClosest_1(self, nums, target):
        """
        参考思路:https://leetcode.com/problems/3sum-closest/solution/
        先把问题转化为two sum closest问题,然后采用Two Pointers approach思路,通过sum和target的大小比较进行lo和hi指针的移动.
        PS:采用abs之后会丢失原本的数字的有序性,导致无法使用双指针夹逼法.
        具体算法如下:
        1.Initialize the minimum difference diff with a large value.
        2.Sort the input array nums.
        3.Iterate through the array:
            a.For the current position i, set lo to i + 1, and hi to the last index.
            b.While the lo pointer is smaller than hi:
                Set sum to nums[i] + nums[lo] + nums[hi].
                If the absolute difference between sum and target is smaller than the absolute value of diff:
                    Set diff to target - sum.
                If sum is less than target, increment lo.
                Else, decrement hi.
            c.If diff is zero, break from the loop.
        4.Return the value of the closest triplet, which is target - diff.
        -----------
        验证通过:
        Runtime: 116 ms, faster than 88.31% of Python3 online submissions for 3Sum Closest.
        Memory Usage: 14 MB, less than 18.93% of Python3 online submissions for 3Sum Closest.
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return None
        nums.sort()
        diff = sys.maxsize
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                t_sum = nums[i] + nums[lo] + nums[hi]
                if t_sum == target:
                    return t_sum
                if t_sum > target:
                    hi -= 1
                else:
                    lo += 1
                diff = target - t_sum if abs(diff) > abs(target - t_sum) else diff
        # 由diff = target - t_sum等式可以得出t_sum=target - diff
        return target - diff

    def threeSumClosest_brute(self, nums, target):
        """
        暴力法.也可以使用递归,使之转化为NSumClosest问题
        时间复杂度:O(N**3)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 3:
            return None
        ret = 0
        cache = sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    t_sum = nums[i] + nums[j] + nums[k]
                    if cache > abs(target - t_sum):
                        cache = abs(target - t_sum)
                        ret = t_sum
        return ret


def main():
    nums = [-1, 2, 1, -4]
    target = 1
    ret = Solution().threeSumClosest(nums, target)
    print(ret)
    print(ret == 2)
    print('--------------------')


if __name__ == "__main__":
    main()
