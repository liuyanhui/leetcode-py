"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.search_1(nums, target)

    def search_1(self, nums: List[int], target: int) -> bool:
        """
        Round 3
        Score[1] Lower is harder

        Thinking：
        1. one-pass solution
        遍历并查找
        时间复杂度:O(N)
        2. binary search + 分类判断法（分四种情况）
        review review binary search 的判断条件是left,mid和right，而不是target。这个细节很重要

        验证通过：
        Runtime 60 ms Beats 11.35%
        Memory 17.14 MB Beats 61.06%
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            # review 跳过收尾相同的数字
            while i < j and nums[i] == nums[i + 1]:
                i += 1
            while i < j and nums[j - 1] == nums[j]:
                j -= 1

            mid = (i + j) // 2
            if nums[mid] == target:
                return True
            # review binary search 的判断条件是left,mid和right，而不是target。这个细节很重要
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return False


def do_func(nums: List[int], target: int, expect: bool):
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == expect)
    assert ret == expect
    print("---------------------")


def main():
    do_func(nums=[2, 5, 6, 0, 0, 1, 2], target=0, expect=True)
    do_func(nums=[2, 5, 6, 0, 0, 1, 2], target=3, expect=False)
    do_func(nums=[3, 1], target=1, expect=True)
    do_func(nums=[12], target=1, expect=False)
    do_func(nums=[1, 3, 1, 1, 1], target=1, expect=True)
    do_func(nums=[1, 3, 1, 1, 1], target=3, expect=True)
    do_func(nums=[1, 1, 1, 1, 1], target=1, expect=True)
    do_func(nums=[1, 1, 1, 1, 1], target=22, expect=False)
    do_func(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2, expect=True)
    do_func(nums=[3, 5, 1], target=3, expect=True)
    do_func(nums=[5, 1, 3], target=3, expect=True)
    print('----Done----')


if __name__ == "__main__":
    main()
