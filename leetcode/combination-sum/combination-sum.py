class Solution:
    """
    https://leetcode.com/problems/combination-sum/
    39. Combination Sum
    Medium
    """

    def combinationSum(self, candidates, target):
        if candidates is None or len(candidates) == 0 or target < 0:
            return []
        ret = []
        self.findTheResult_2(candidates, 0, target, [], ret)
        return ret

    def findTheResult_1(self, nums, beg, target, present, ret):
        """
        采用Combination的思路,采用递归方法进行计算.
        思路描述:
        第i个数字nums[i],从1~target/nums[i]进行遍历(代表nums[i]重复出现的情况),然后nums[i+1]从1~(target-num[i]*k)进行递归.
        :param nums:原始数组
        :param beg: 开始处理的下标
        :param target: target余额
        :param present: 中间变量
        :param ret: 最终结果
        :return:
        """
        if target == 0:
            ret.append(present.copy())
            return
        if target <= 0 or beg >= len(nums):
            return

        for i in range(beg, len(nums)):
            for k in range(1, target // nums[i] + 1):
                # 某个数字重复出现的情况
                for j in range(k):
                    present.append(nums[i])
                # 递归处理剩下的target余额
                self.findTheResult_1(nums, i + 1, target - (nums[i] * k), present, ret)
                # 出栈后回退present
                for j in range(k):
                    present.remove(nums[i])

    def findTheResult_2(self, nums, beg, target, present, ret):
        """
        findTheResult_1方法的简化版,通过target - nums[i]替代findTheResult_1中的nums[i]重复出现的情况
        :param nums:原始数组
        :param beg: 开始处理的下标
        :param target: target余额
        :param present: 中间变量
        :param ret: 最终结果
        :return:
        """
        if target == 0:
            ret.append(present.copy())
            return
        if target <= 0 or beg >= len(nums):
            return

        for i in range(beg, len(nums)):
            present.append(nums[i])
            self.findTheResult_2(nums, i, target - nums[i], present, ret)
            present.remove(nums[i])



def main():
    a = [2, 3, 6, 7]
    target = 7
    ret = Solution().combinationSum(a, target)
    print(ret)
    print("-------------")

    a = [2, 3, 5]
    target = 8
    ret = Solution().combinationSum(a, target)
    print(ret)
    print("-------------")


if __name__ == "__main__":
    main()
