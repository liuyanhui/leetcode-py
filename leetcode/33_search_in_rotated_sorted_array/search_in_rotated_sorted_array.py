"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
33. Search in Rotated Sorted Array
Medium
---------------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        return self.search_1(nums, target)

    def search_1(self, nums, target):
        """
        参考思路:
        https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
        用了一种更加简单的判断方法.这种判断一目了然
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 左半部分有序
            if nums[l] <= nums[mid]:
                # target在左半部分
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # target在右半部分
                else:
                    l = mid + 1
            # 有半部分有序
            else:
                # target在右半部分
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # target在左半部分
                else:
                    r = mid - 1
        return -1

    def search_error(self, nums, target):
        """
        验证失败,判断逻辑比较复杂,并且有隐患.
        用例nums = [3,1],target = 1未通过.
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if nums[mid] == target:
                return mid
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target <= nums[r]:
                l = mid + 1
            elif nums[l] < nums[mid] < target or target < nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == 4)
    print('--------------------')

    nums = [1, 2, 3]
    target = 1
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == 0)
    print('--------------------')

    nums = [3, 1]
    target = 1
    ret = Solution().search(nums, target)
    print(ret)
    print(ret == 1)
    print('--------------------')


if __name__ == "__main__":
    main()
