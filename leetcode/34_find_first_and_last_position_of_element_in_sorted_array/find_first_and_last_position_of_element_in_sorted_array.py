"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. Find First and Last Position of Element in Sorted Array
Medium
---------------
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        验证通过:
        Runtime: 84 ms, faster than 85.06% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
        Memory Usage: 15 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        ret = [-1, -1]

        def cut_left(n, m):
            while m > 0 and n[m] == n[m - 1]:
                m -= 1
            return m

        def cut_right(n, m):
            while m < len(n) - 1 and n[m] == n[m + 1]:
                m += 1
            return m

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ret[0] = cut_left(nums, mid)
                ret[1] = cut_right(nums, mid)
                return ret
            elif nums[mid] > target:
                r = cut_left(nums, mid)
                r -= 1
            else:
                l = cut_right(nums, mid)
                l += 1
        return ret


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    ret = Solution().searchRange(nums, target)
    print([3, 4])
    print(ret == [3, 4])
    print('--------------------')

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    ret = Solution().searchRange(nums, target)
    print([-1, -1])
    print(ret == [-1,-1])
    print('--------------------')


    nums = [5]
    target = 5
    ret = Solution().searchRange(nums, target)
    print([0, 0])
    print(ret == [0,0])
    print('--------------------')

    nums = [5]
    target = 6
    ret = Solution().searchRange(nums, target)
    print([-1, -1])
    print(ret == [-1,-1])
    print('--------------------')


if __name__ == "__main__":
    main()
