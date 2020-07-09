"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
154. Find Minimum in Rotated Sorted Array II
Hard
--------------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution:
    def findMin(self, nums):
        return self.findMin_2(nums)

    def findMin_2(self, nums):
        """
        这个解法,直接使用原始的binary search.
        更容易理解,实现也更简单.
        参考思路:
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/725072/Python3-minimum-in-rotated-sorted-array-I-and-II
        :param nums:
        :return:
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]

    def findMin_1(self, nums):
        """
        binary search的思路,但是需要考虑特殊情况
        验证通过:
        Runtime: 72 ms, faster than 20.55% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
        Memory Usage: 14.3 MB, less than 50.95% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            # 如果已经是排序好的直接返回第一个元素即可
            if nums[l] < nums[r]:
                break
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid + 1
            else:
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # 这里需要考虑两种情况:
                # 1.只有两个元素,并且相等的情况
                # 2.只有两个袁术,前大后小
                l = (l + 1 if l < r else l)
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
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

    nums = [1, 3, 5]
    ret = Solution().findMin(nums)
    print(ret)
    print(ret == 1)
    print('--------------------')

    nums = [2, 2, 2, 0, 1]
    ret = Solution().findMin(nums)
    print(ret)
    print(ret == 0)
    print('--------------------')

    nums = [0, 0, 0, 0, 0, 0]
    ret = Solution().findMin(nums)
    print(ret)
    print(ret == 0)
    print('--------------------')


if __name__ == "__main__":
    main()
