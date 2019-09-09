import collections


class Solution:
    """
    https://leetcode.com/problems/number-of-squareful-arrays/
    996. Number of Squareful Arrays
    Hard
    ------------
    Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
    Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
    Example 1:
    Input: [1,17,8]
    Output: 2
    Explanation:
    [1,8,17] and [17,8,1] are the valid permutations.

    Example 2:
    Input: [2,2,2]
    Output: 1
     Note:
    1 <= A.length <= 12
    0 <= A[i] <= 1e9
    """

    def numSquarefulPerms(self, A):
        return self.numSquarefulPerms_2(A)

    def numSquarefulPerms_1(self, A):
        """
        该方法采用了permutation的思路.
        验证失败,原因: Time Limit Exceeded,用例为[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        :param A:
        :return:
        """
        if not A or len(A) == 0:
            return 0
        # 增加了所有元素都是2的特殊情况处理,可以防止Time Limit Exceeded --beg
        # 输入为[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]时,Time Limit Exceeded
        for i in range(len(A)):
            if A[i] != 2:
                break
            if i == len(A) - 1:
                return 1
        # 增加了所有元素都是2的特殊情况处理,可以防止Time Limit Exceeded --end

        ret = [0]
        existed = set()

        def permutaion_and_calc(A, beg, present, ret):
            if len(present) >= 2:
                if not isSquareful(present[-1], present[-2]):
                    return
            if len(present) == len(A):
                if str(present) not in existed:
                    existed.add(str(present))
                    ret[0] += 1
            for i in range(beg, len(A)):
                present.append(A[i])
                swap(A, i, beg)
                permutaion_and_calc(A, beg + 1, present, ret)
                swap(A, beg, i)
                # 这里不能用present.remove(A[i]),因为A[i]可能会重复,导致第一个与A[i]相等的数字被删除
                present.pop()

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def isSquareful(i, j):
            if int(((i + j) ** 0.5)) ** 2 == i + j:
                return True
            else:
                return False

        permutaion_and_calc(A, 0, [], ret)
        return ret[0]

    def numSquarefulPerms_2(self, A):
        """
        参考思路:
        https://leetcode.com/problems/number-of-squareful-arrays/discuss/238562/C%2B%2BPython-Backtracking

        1.Count numbers occurrence.
        2.For each number i, find all possible next number j that i + j is square.
        3.Backtracking using dfs.
        :param A:
        :return:
        """
        if not A or len(A) == 0:
            return 0
        self.ret = 0
        c = collections.Counter(A)
        cand = {i: {j for j in A if int((i + j) ** 0.5) ** 2 == i + j} for i in A}

        def dfs(x, left):
            if left == 0:
                self.ret += 1
            c[x] -= 1
            for y in cand[x]:
                if c[y]:
                    dfs(y, left - 1)
            c[x] += 1

        # 这里是关键,如果把c换成A,会对A中重复出现的数字进行遍历,导致重复基数
        for x in c:
            dfs(x, len(A) - 1)
        return self.ret


def main():
    A = [1, 8, 17]
    ret = Solution().numSquarefulPerms(A)
    print(ret)
    print("----------")

    A = [2, 2, 2]
    ret = Solution().numSquarefulPerms(A)
    print(ret)
    print("----------")

    A = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ret = Solution().numSquarefulPerms(A)
    print(ret)
    print("----------")

    A = [80, 1, 80, 1, 3, 6, 3]
    ret = Solution().numSquarefulPerms(A)
    print(ret)
    print("----------")

    A = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ret = Solution().numSquarefulPerms(A)
    print(ret)
    print("----------")

if __name__ == "__main__":
    main()
