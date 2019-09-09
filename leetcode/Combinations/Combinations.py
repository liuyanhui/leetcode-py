class Solution:
    """
    https://leetcode.com/problems/combinations/
    77. Combinations
    Medium
    """

    def combine(self, n, k):
        nums = list(range(1, n + 1))
        # print(nums)
        ret = []
        self.combine_recursive(nums, k, 0, ret, [])
        return ret

    def combine_recursive(self, nums, count, beg, ret=[], present=[]):
        """
        跟Permutation的区别:
        permutation需要排列,所以不能使用下标将参与计算的数字排除;combination不需要排列,本身就是有序的,所以可以通过下标排除已经计算过得数字

        :param nums: 当前数组
        :param count: 剩余组合中数字的个数
        :param beg: 开始的下标
        :param ret: 最终结果
        :param present: 中间结果
        :return:
        """
        if count == 0:
            ret.append(present.copy())
            return
        for i in range(beg, len(nums)):
            present.append(nums[i])
            self.combine_recursive(nums, count - 1, i + 1, ret, present)
            present.remove(nums[i])


def main():
    n, k = 5, 2
    ret = Solution().combine(n, k)
    print(str(ret))


if __name__ == "__main__":
    main()
