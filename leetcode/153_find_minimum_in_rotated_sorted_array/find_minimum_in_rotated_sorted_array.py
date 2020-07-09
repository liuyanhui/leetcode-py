"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
153. Find Minimum in Rotated Sorted Array
Medium
----------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums):
        """
        典型的binary search问题
        验证通过:
        Runtime: 48 ms, faster than 25.55% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
        Memory Usage: 14 MB, less than 71.13% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] > nums[r]:
                mid = (l + r) // 2
                if nums[l] > nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                return nums[l]
        return nums[l]


def main():
    nums = [3, 4, 5, 1, 2]
    ret = Solution().findMin(nums)
    print(ret)
    print(ret == 1)
    print('--------------------')

    nums = [3, 4, 5, 6, 7, 8, 9, 1, 2]
    ret = Solution().findMin(nums)
    print(ret)
    print(ret == 1)
    print('--------------------')


if __name__ == "__main__":
    main()
