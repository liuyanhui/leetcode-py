"""
https://leetcode.com/problems/find-peak-element/
162. Find Peak Element
Medium
---------------
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

Follow up: Your solution should be in logarithmic complexity.
"""
import sys


class Solution:
    def findPeakElement(self, nums):
        return self.findPeakElement_ref2(nums)

    def findPeakElement_binarysearch(self, nums):
        """
        binary search思路.
        1.需要考虑nums[-1]和nums[n]这两种边界值.
        2.使用二分查找的算法得到数组中间下标 m
        3.当nums[m-1]<nums[m]>nums[m+1]时,返回m
        4.当nums[m-1]<nums[m]<nums[m+1]时,认为所求一定在nums[m]~nums[n-1]之间
        5.当nums[m-1]>nums[m]>nums[m+1]时,认为所求一定在nums[0]~nums[m]之间
        6.循环步骤2到步骤6
        ---------------
        验证通过:
        Runtime: 68 ms, faster than 17.20% of Python3 online submissions for Find Peak Element.
        Memory Usage: 13.8 MB, less than 87.05% of Python3 online submissions for Find Peak Element.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return -1
        MIN_INT = -sys.maxsize - 1
        l, r = -1, len(nums)
        while l <= r:
            m = (l + r) // 2
            a = MIN_INT if m == 0 else nums[m - 1]
            b = MIN_INT if m == len(nums) - 1 else nums[m + 1]
            if a < nums[m] > b:
                return m
            elif a < nums[m] < b:
                l = m
            else:
                r = m
        return -1

    def findPeakElement_brtue(self, nums):
        """
        暴力法,通过滑动窗口解决
        ---------------
        验证通过:
        Runtime: 56 ms, faster than 27.99% of Python3 online submissions for Find Peak Element.
        Memory Usage: 13.9 MB, less than 83.22% of Python3 online submissions for Find Peak Element.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return -1
        MIN_INT = -sys.maxsize - 1
        for i in range(len(nums)):
            l = MIN_INT if i == 0 else nums[i - 1]
            r = MIN_INT if i == len(nums) - 1 else nums[i + 1]
            if l < nums[i] > r:
                return i
        return -1

    def findPeakElement_ref1(self, nums):
        """
        不需要计算类似nums[m-1]<nums[m]>nums[m+1]的情况,只需要计算nums[m]>nums[m+1]即可
        参考思路:https://leetcode.com/problems/find-peak-element/solution/
        ----------
        验证通过:
        Runtime: 84 ms, faster than 6.91% of Python3 online submissions for Find Peak Element.
        Memory Usage: 14 MB, less than 49.57% of Python3 online submissions for Find Peak Element.
        :param nums:
        :return:
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findPeakElement_ref2(self, nums):
        """
        findPeakElement_ref1的binary search方法
        参考思路:https://leetcode.com/problems/find-peak-element/solution/
        -----------
        验证通过:
        Runtime: 40 ms, faster than 94.05% of Python3 online submissions for Find Peak Element.
        Memory Usage: 14 MB, less than 50.56% of Python3 online submissions for Find Peak Element.
        :param nums:
        :return:
        """
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m+1

        return l


def main():
    nums = [1, 2, 3, 1]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [2])
    print('--------------------')

    nums = [1, 2, 1, 3, 5, 6, 4]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [1, 5])
    print('--------------------')

    nums = [1]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [0])
    print('--------------------')

    nums = [1, 2]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [1])
    print('--------------------')

    nums = [1, 2, 3]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [2])
    print('--------------------')

    nums = [-2147483648]
    ret = Solution().findPeakElement(nums)
    print(ret)
    print(ret in [0])
    print('--------------------')


if __name__ == "__main__":
    main()
