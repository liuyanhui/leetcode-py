"""
https://leetcode.com/problems/two-sum/
1. Two Sum
Easy
----------
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import collections


class Solution:
    def twoSum(self, nums, target):
        return self.twoSum_3(nums, target)

    def twoSum_3(self, nums, target):
        """
        one pass 方案,只需要遍历一次nums
        验证通过:
        Runtime: 40 ms, faster than 98.55% of Python3 online submissions for Two Sum.
        Memory Usage: 15.2 MB, less than 44.33% of Python3 online submissions for Two Sum.
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        cache = {}
        MAX_INT = 9999999
        for i in range(len(nums)):
            if cache.get(target - nums[i], MAX_INT) == MAX_INT:
                cache[nums[i]] = i
            else:
                return [cache[target - nums[i]], i]

    def twoSum_2(self, nums, target):
        """
        two pass 方案,即需要遍历两次nums
        验证通过:
        Runtime: 68 ms, faster than 44.68% of Python3 online submissions for Two Sum.
        Memory Usage: 16 MB, less than 6.09% of Python3 online submissions for Two Sum.
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        MAX_INT = 9999999
        v_i_cache = {}
        for i in range(len(nums)):
            v_i_cache[nums[i]] = i

        for i in range(len(nums)):
            if v_i_cache.get(target - nums[i], MAX_INT) != MAX_INT and i != v_i_cache[target - nums[i]]:
                return [i, v_i_cache[target - nums[i]]]
        return []

    def twoSum_1(self, nums, target):
        """
        验证失败,无法处理重复出现的元素
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        v_i_cache = {}
        for i in range(len(nums)):
            v_i_cache[nums[i]] = i
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [v_i_cache[nums[l]], v_i_cache[nums[r]]]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    ret = Solution().twoSum(nums, target)
    print(ret)
    print(ret == [0, 1])
    print("---------------------")

    nums = [4, 4]
    target = 8
    ret = Solution().twoSum(nums, target)
    print(ret)
    print(ret == [0, 1])
    print("---------------------")

    nums = [3, 2, 4]
    target = 6
    ret = Solution().twoSum(nums, target)
    print(ret)
    print(ret == [1, 2])
    print("---------------------")

    nums = [2, 7, 11, 15, 3, 5]
    target = 8
    ret = Solution().twoSum(nums, target)
    print(ret)
    print(ret == [4, 5])
    print("---------------------")


if __name__ == "__main__":
    main()
