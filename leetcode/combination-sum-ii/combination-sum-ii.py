class Solution:
    """
    https://leetcode.com/problems/combination-sum-ii/
    40. Combination Sum II
    Medium
    """

    def combinationSum2(self, candidates, target):
        ret = []
        self.combinationSum2_1(candidates, target, 0, [], ret)
        return ret

    def combinationSum2_1(self, candidates, target, beg, present, ret):
        if target < 0:
            return
        if target == 0:
            # 去重
            existed = False
            tmp_present = present.copy()
            tmp_present.sort()
            for r in ret:
                if len(r) == len(tmp_present):
                    for i in range(len(r)):
                        if r[i] != tmp_present[i]:
                            break
                        if i == len(r) - 1:
                            existed = True
            if not existed:
                ret.append(tmp_present)
            return ret

        for i in range(beg, len(candidates)):
            present.append(candidates[i])
            self.combinationSum2_1(candidates, target - candidates[i], i + 1, present, ret)
            present.remove(candidates[i])


def main():
    a = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    ret = Solution().combinationSum2(a, t)
    print(ret)
    print("------------")

    a = [2, 5, 2, 1, 2]
    t = 5
    ret = Solution().combinationSum2(a, t)
    print(ret)
    print("------------")


if __name__ == "__main__":
    main()
