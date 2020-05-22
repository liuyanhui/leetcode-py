"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
81. Search in Rotated Sorted Array II
Medium
---------------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution:
    def search(self, nums, target):
        return self.search_2(nums, target)

    def search_2(self, nums, target):
        """
        另一个版本,思路如下:
        https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 这里是关键点.只要能打破当前的平衡,能推进程序向目标前进的就行.
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # 下面被注释的是错误的
            # if l < mid and nums[mid] == nums[mid - 1]:
            #     mid -= 1

            # binary search的逻辑
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    def search_1(self, nums, target):
        """
        跟问题33. Search in Rotated Sorted Array的思路相似,只不过增加了mid附件重复数据的排除逻辑.
        ------------
        验证通过:
        Runtime: 56 ms, faster than 52.30% of Python3 online submissions for Search in Rotated Sorted Array II.
        Memory Usage: 14 MB, less than 5.72% of Python3 online submissions for Search in Rotated Sorted Array II.
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 避免只剩一个元素时死循环
            if l == r:
                return False
            mid_l, mid_r = mid, mid
            # 排除mid左边的重复数字
            while mid_l > l and nums[mid_l] == nums[mid_l - 1]:
                mid_l -= 1
            # 因为nums[mid]已经被排除,所以跳过mid处的数字
            if mid_l > l:
                mid_l -= 1
            # 排除mid右边的重复数字
            while mid_r < r and nums[mid_r] == nums[mid_r + 1]:
                mid_r += 1
            # 因为nums[mid]已经被排除,所以跳过mid处的数字
            if mid_r < r:
                mid_r += 1
            # binary search的逻辑
            if nums[l] <= nums[mid_l]:
                if nums[l] <= target <= nums[mid_l]:
                    r = mid_l
                else:
                    l = mid_r
            else:
                if nums[mid_r] <= target <= nums[r]:
                    l = mid_r
                else:
                    r = mid_l
        return False


def main():
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == True)
    print('--------------------')

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    nums = [3, 1]
    target = 1
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == True)
    print('--------------------')

    nums = [12]
    target = 1
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == False)
    print('--------------------')

    nums = [1, 3, 1, 1, 1]
    target = 3
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == True)
    print('--------------------')


if __name__ == "__main__":
    main()
