class Solution:
    """
    https://leetcode.com/problems/permutations/
    46. 46_Permutations
    Medium
    """

    def permute(self, nums):
        return  self.permute_2(nums)

    def permute_1(self, nums):
        """
        需要用到回溯法(backtracking)
        :param nums:
        :return:
        """
        if nums is None or len(nums) == 0:
            return None
        ret = []
        self.permute_child(nums, ret, [])
        return ret

    def permute_child(self, nums, ret, present=[]):
        """
        递归法,思路如下:
        P(n)=n*P(n-1)
        :param nums: 未参加排列的剩余数字
        :param ret: 最终结果
        :param present: 中间变量
        :return:
        """
        if nums is None or len(nums) == 0:
            ret.append(present.copy())
            return present
        for i in range(len(nums)):
            present += [nums[i]]
            tmp_nums = nums.copy()
            tmp_nums.remove(nums[i])
            self.permute_child(tmp_nums, ret, present)
            present.remove(nums[i])

    def permute_2(self, nums):
        """
        另一种递归的思路.
        与permute_1不同之处:不采用中间变量进行中间结果的存储,通过数组元素的交换的方式保存中间结果
        参考文档:
        https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51534048
        https://blog.csdn.net/zxzxzx0119/article/details/81452269
        :param nums:
        :return:
        """
        ret = []
        self.permute_child_2(nums, 0, ret)
        return ret

    def permute_child_2(self, nums, i, ret):
        if i == len(nums):
            ret.append(nums)
            return
        for j in range(i, len(nums)):
            self.swap(nums, i, j)
            self.permute_child_2(nums, i + 1, ret)
            self.swap(nums, j, i)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


def main():
    nums = [1, 2, 3]
    ret = Solution().permute(nums)
    print(ret)

    nums = [1, 2, 3]
    ret = Solution().permute_1(nums)
    print(str(ret))

    # Solution().swap(nums, 1, 2)
    # print(str(nums))


if __name__ == "__main__":
    main()
