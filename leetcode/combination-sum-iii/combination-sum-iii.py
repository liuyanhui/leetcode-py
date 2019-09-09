class Solution:
    """
    https://leetcode.com/problems/combination-sum-iii/
    216. Combination Sum III
    Medium
    """

    def combinationSum3(self, k, n):
        arr = [i for i in range(1, 10)]
        ret = []
        self.findCombinationSum(arr, k, n, 0, [], ret)
        return ret

    def findCombinationSum(self, arr, count, target, beg, present, ret):
        if len(present) > count or target < 0:
            return
        if target == 0 and len(present) == count:
            ret.append(present.copy())
            return

        for i in range(beg, len(arr)):
            present.append(arr[i])
            self.findCombinationSum(arr, count, target - arr[i], i + 1, present, ret)
            present.remove(arr[i])


def main():
    k = 3
    n = 7
    ret = Solution().combinationSum3(k, n)
    print(ret)
    print("-------------")

    k = 3
    n = 9
    ret = Solution().combinationSum3(k, n)
    print(ret)
    print("-------------")

    k = 2
    n = 18
    ret = Solution().combinationSum3(k, n)
    print(ret)
    print("-------------")


if __name__ == '__main__':
    main()
