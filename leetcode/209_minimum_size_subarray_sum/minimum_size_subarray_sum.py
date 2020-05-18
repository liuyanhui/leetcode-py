"""
https://leetcode.com/problems/minimum-size-subarray-sum/
209. Minimum Size Subarray Sum
Medium
--------------
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        return self.minSubArrayLen_slide_2(s, nums)

    def minSubArrayLen_slide_2(self, s, nums):
        """
        minSubArrayLen_slide的代码简化版.
        巧妙的用while语句替换了minSubArrayLen_slide()中的if语句.
        :param s:
        :param nums:
        :return:
        """
        total, left = 0, 0
        ret = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                ret = min(ret, right - left + 1)
                total -= nums[left]
                left += 1
        return ret if ret <= len(nums) else 0

    def minSubArrayLen_slide(self, s, nums):
        """
        滑动窗口思路,有两个指针i和j.
        当sum[i:j]>=s时 ==> sum-=sum[i],i+1,ret=min(ret,j-i+1)
        当sum[i:j] <s时 ==> j+1,sum+=num[j]
        需要注意边界
        -------------
        Time Complexity:O(N)
        验证通过
        Runtime: 80 ms, faster than 48.55% of Python3 online submissions for Minimum Size Subarray Sum.
        Memory Usage: 16.4 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
        :param s:
        :param nums:
        :return:
        """
        if s <= 0 or not nums:
            return 0
        ret = 9999999
        i, j = 0, 0
        sum_t = nums[0]
        while j < len(nums):
            if sum_t >= s:
                ret = min(ret, j - i + 1)
                sum_t -= nums[i]
                i += 1
                continue
            else:
                j += 1
                if j < len(nums):
                    sum_t += nums[j]
        if j >= len(nums) and i == 0:
            ret = 0
        return ret

    def minSubArrayLen_brute(self, s, nums):
        """
        最简单的暴力法
        -----
        验证超时,
        Time Complexity:O(N*N)
        :param s:
        :param nums:
        :return:
        """
        if s <= 0 or not nums:
            return 0
        ret = 9999999
        for i in range(len(nums)):
            index_t = i
            sum_t = 0
            while sum_t < s and index_t < len(nums):
                sum_t += nums[index_t]
                index_t += 1
            if sum_t >= s:
                ret = min(ret, index_t - i)
            elif ret == 9999999:
                ret = 0
                break

        return ret


def main():
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    ret = Solution().minSubArrayLen(s, nums)
    print(ret)
    print(ret == 2)
    print("------------------")

    s = 15
    nums = [1, 2, 4, 3]
    ret = Solution().minSubArrayLen(s, nums)
    print(ret)
    print(ret == 0)
    print("------------------")


if __name__ == "__main__":
    main()
